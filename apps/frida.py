"""
/**
 * hook导出的加密函数的参数,
 * so里面共传入两个参数,参数1 为要加密的内容, 参数2 为AES ECB模式的key
 * //frida -U --no-pause -f com.shizhuang.duapp -l dewu.js
 *  --no-pause是即时hook
 *  --no-pause 自动运行程序
 *
 *  -f是通过spawn，也就是重启apk注入js
 *  -f 指定一个进程，重启它并注入脚本
 *
 *   -U, --usb             connect to USB device
 *   -l 指定加载一个Javascript脚本
 */

frida其他操作
# 查看当前手机运行APP
adb shell dumpsys window | findstr mCurrentFocus

# frida 端口转发
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

更名: 将frida-server改名为fenfeiserver
改端口: 手机里面用 fenfeiserver -l 127.0.0.1:8080 来启动
电脑里面先映射 adb forward tcp:8080 tcp:8080
然后启动 frida -H 127.0.0.1:8080 -l jd.js com.jingdong.app.mall
"""