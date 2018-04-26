let cnt = 1;
let colortCnt = 0;
const colorList = ['rgb(248, 164, 164)',
                    'rgb(163, 163, 248)',
                    'rgb(250, 250, 124)'];
$(function() {
    $('.add-btn').on('click', () => {
        $('.task-list').append(
            `<li class='task'>${cnt}個目の追加
            <button class="del-btn">削除</button>
            <button class="ch-color">色変更</button>
            </li>`
        );
        cnt += 1;
    });

    $('.task-list').on('click', '.del-btn', (evt) => {
        $(evt.currentTarget).parent().remove();
    });

    $('.task-list').on('click', '.ch-color', (evt) => {
        let color = colorList[colortCnt];
        $(evt.currentTarget).parent().css({background: color});
        colortCnt += 1;
        if (colortCnt === colorList.length) {
            colortCnt = 0;
        }
    });
})