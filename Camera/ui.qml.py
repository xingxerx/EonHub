import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: mainWindow
    width: 800
    height: 600
    visible: true
    title: qsTr("Camera App")

    Image {
        id: cameraView
        anchors.fill: parent
        sourceSize.width: parent.width
        sourceSize.height: parent.height
        fillMode: Image.PreserveAspectFit
    }

    Column {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        spacing: 10
        padding: 10

        Switch {
            id: superpositionSwitch
            text: "Superposition"
            checked: backend.isSuperpositionEnabled
            onCheckedChanged: backend.isSuperpositionEnabled = checked
        }

        Button {
            text: "Get Random Number"
            onClicked: backend.getRandomNumber(8) // Example: 8-bit random number
        }
    }
    Connections {
        target: backend
        function onFrameChanged(frame) {
            cameraView.source = frame
        }
    }
}
