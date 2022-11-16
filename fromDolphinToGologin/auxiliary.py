# Auxiliary file

class Auxiliary:
    def __init__(self, result):
        self.result = result

    def getTags(self):
        if self.result['data']['tags'] == []:
            return False
        else:
            tags = self.result['data']['tags'][0]
            return tags

    def getOs(self):
        if self.result['data']['platform'] == 'windows':
            os = 'win'
            return os
        elif self.result['data']['platform'] == 'macos':
            platform = 'mac'
            return platform
        elif self.result['data']['platform'] == 'linux':
            platform = 'lin'
            return platform

    def getWebrtc(self):
        if self.result['data']['webrtc']['mode'] == 'altered' or 'manual':
            mode = 'alerted'
            return mode
        elif self.result['data']['webrtc']['mode'] == 'off':
            mode = 'disabled'
            return mode
        else:
            mode = 'real'
            return mode

    def getCanvas(self):
        if self.result['data']['canvas']['mode'] == 'real':
            canvas = 'off'
            return canvas
        elif self.result['data']['canvas']['mode'] == 'off':
            canvas = 'off'
            return canvas
        elif self.result['data']['canvas']['mode'] == 'noise':
            canvas = 'noise'
            return canvas

    def getWebgl(self):
        if self.result['data']['webgl']['mode'] == 'real':
            webgl = 'off'
            return webgl
        elif self.result['data']['webgl']['mode'] == 'off':
            webgl = 'off'
            return webgl
        elif self.result['data']['webgl']['mode'] == 'noise':
            webgl = 'noise'
            return webgl

    def getWebGLInfo(self):
        if self.result['data']['webglInfo']['mode'] == 'manual':
            mode = 'mask'
        else:
            mode = 'off'

        return {
            'mode': mode,
            'vendor': self.result['data']['webglInfo']['vendor'],
            'renderer': self.result['data']['webglInfo']['renderer']
        }
    
    def getClientRect(self):
        if self.result['data']['clientRect']['mode'] == 'real':
            clientRect = 'off'
            return clientRect
        else:
            clientRect = 'noise'
            return clientRect
    
    def getProxy(self):
        if self.result['data']['proxyId'] == 0:
            return {
                'mode': 'none'
            }
        else:
            return {
                'mode': self.result['data']['proxy']['type'],
                'host': self.result['data']['proxy']['host'],
                'port': self.result['data']['proxy']['port'],
                'username': self.result['data']['proxy']['login'],
                'password': self.result['data']['proxy']['password']
            }

    