//alert('ddefeferfertgrgr');

    // 目次のクラス名を持つ要素を取得
    // var tocElement = document.querySelector('.toc');

    // // レンダリング先の要素を取得
    // var renderedTocElement = document.querySelector('.rendered-toc');
   
   
    // tocElement.classList.add('.disp-toc')


    // // 目次をコピーして別の領域にレンダリング
    // if (tocElement && renderedTocElement) {
    //     var clonedToc = tocElement.cloneNode(true);
    //     renderedTocElement.appendChild(clonedToc);
    // } 
    
    // tocElement.classList.remove('.toc');  // 旧クラスを削除




        // クラス名を変更してレンダリングしたい元の要素を取得
        var originalElement = document.querySelector('.toc');

        // レンダリング先の要素を取得
        var renderedTocElement = document.querySelector('.rendered-toc');
    
        // 元の要素が存在し、レンダリング先の要素が存在する場合
        if (originalElement && renderedTocElement) {
            // クラス名を変更
            originalElement.classList.add('hidden');
            
            // 元の要素をクローンしてレンダリング先に追加
            var clonedToc = originalElement.cloneNode(true);
            renderedTocElement.appendChild(clonedToc);
        }