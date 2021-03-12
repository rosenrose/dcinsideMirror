function replace(root) {
    let ends = [["구요","고요$1"],["되라","돼라$1"],["되","돼$1"]];
    let replaces = [["(노|놐|누|눜)([.,!?;ㄱ-ㅎ]*)","냐$2"],["(노|놐|누|눜|이기)([.,!?;ㄱ-ㅎ]*)$","냐$2"],
        ["되노","되냐"],["무친","미친"],["무쳤","미쳤"],["노무","너무"],["운지","좆망"],["(했|햇)(노|누)","했냐"]];
    walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    while(node = walk.nextNode()) {
        if (text = node.textContent.trim()) {
            for (let replace of replaces) {
                regex = new RegExp(replace[0], "g");
                if (result = regex.exec(text)) {
                    node.textContent = text.replace(regex, replace[1]);
                    console.log(`${text} (${result[0]})\n-----\n${node.textContent}`);
                    text = node.textContent;
                }
            }
            for (let end of ends) {
                regex = new RegExp(`${end[0]}([.,!?;ㄱ-ㅎ\\s]*)$`, "g")
                if (result = regex.exec(text)) {
                    node.textContent = text.replace(regex, end[1]);
                    console.log(`${text} (${result[0]})\n-----\n${node.textContent}`);
                    text = node.textContent;
                }
            }
        }
    }
}
document.addEventListener("DOMContentLoaded", () => {
    replace(document.body);
    replace(document.head);
});