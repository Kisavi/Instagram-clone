
    $(document).ready(() => {
  const comment = $("#comment");

  comment
    .on("keydown input keyup", function () {
      comment.height(0).height(this.scrollHeight);
      const value = comment.val().trim();
      const post = $("#post");

      if (value.length > 0) {
        post.removeAttr("disabled", "disabled");
      } else {
        post.attr("disabled", "disabled");
      }
    })
    .find(comment)
    .change();
});

