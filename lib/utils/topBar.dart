import 'package:ibr/ibr.dart';

class TopBar extends StatelessWidget implements PreferredSizeWidget {
  final String title;
  final Color bgColor;
  final bool displayGoBackButton;
  final bool displayActionButton;
  final String actionButtonText;
  final String actionButtonLink;
  const TopBar(
      {Key key,
      this.title,
      this.bgColor,
      this.displayGoBackButton,
      this.displayActionButton,
      this.actionButtonText,
      this.actionButtonLink});
  @override
  Size get preferredSize => new Size.fromHeight(kToolbarHeight);
  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.topRight,
      child: Container(
          padding: EdgeInsets.only(left: 16, right: 16),
          height: 56,
          color: bgColor ?? Colors.transparent,
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              buildGoBackButton(context),
              Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Text(this.title ?? "",
                        style: TextStyle(
                            color: onSurfaceHighEmphasis,
                            fontSize: 20,
                            fontWeight: FontWeight.w500))
                  ]),
              Spacer(),
              buildAppBarButton(context)
            ],
          )),
    );
  }

  Column buildAppBarButton(BuildContext context) {
    return this.displayActionButton
        ? Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              GestureDetector(
                  child: Text(this.actionButtonText,
                      style: TextStyle(
                          color: myTheme.primaryColor,
                          fontSize: 16,
                          fontWeight: FontWeight.normal)),
                  onTap: () {
                    Navigator.pushNamed(context, this.actionButtonLink);
                  }),
            ],
          )
        : Column(
            children: [],
          );
  }

  Container buildGoBackButton(BuildContext context) {
    return this.displayGoBackButton
        ? Container(
            margin: EdgeInsets.only(left: 16),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                GestureDetector(
                  child: IconButton(
                      icon: Icon(Icons.arrow_back_ios, size: 24),
                      onPressed: () {
                        Navigator.pop(context);
                      }),
                ),
              ],
            ),
          )
        : Container();
  }
}
