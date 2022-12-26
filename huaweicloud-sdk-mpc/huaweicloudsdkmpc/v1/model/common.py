# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Common:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pvc': 'bool',
        'hls_interval': 'int',
        'dash_interval': 'int',
        'pack_type': 'int'
    }

    attribute_map = {
        'pvc': 'PVC',
        'hls_interval': 'hls_interval',
        'dash_interval': 'dash_interval',
        'pack_type': 'pack_type'
    }

    def __init__(self, pvc=None, hls_interval=None, dash_interval=None, pack_type=None):
        """Common

        The model defined in huaweicloud sdk

        :param pvc: 是否开启高清低码功能。  取值如下： - false：关闭。 - true：开启。 
        :type pvc: bool
        :param hls_interval: HLS分片间隔，仅封装类型“pack_type”取值为1或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 
        :type hls_interval: int
        :param dash_interval: DASH间隔，仅封装类型“pack_type”取值为2或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 
        :type dash_interval: int
        :param pack_type: 封装类型。  取值如下： - 1：HLS - 2：DASH - 3：HLS+DASH - 4：MP4 - 5：MP3 - 6：ADTS  &gt; pack_type设置为5和6时，不能设置视频参数。 
        :type pack_type: int
        """
        
        

        self._pvc = None
        self._hls_interval = None
        self._dash_interval = None
        self._pack_type = None
        self.discriminator = None

        if pvc is not None:
            self.pvc = pvc
        if hls_interval is not None:
            self.hls_interval = hls_interval
        if dash_interval is not None:
            self.dash_interval = dash_interval
        self.pack_type = pack_type

    @property
    def pvc(self):
        """Gets the pvc of this Common.

        是否开启高清低码功能。  取值如下： - false：关闭。 - true：开启。 

        :return: The pvc of this Common.
        :rtype: bool
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this Common.

        是否开启高清低码功能。  取值如下： - false：关闭。 - true：开启。 

        :param pvc: The pvc of this Common.
        :type pvc: bool
        """
        self._pvc = pvc

    @property
    def hls_interval(self):
        """Gets the hls_interval of this Common.

        HLS分片间隔，仅封装类型“pack_type”取值为1或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 

        :return: The hls_interval of this Common.
        :rtype: int
        """
        return self._hls_interval

    @hls_interval.setter
    def hls_interval(self, hls_interval):
        """Sets the hls_interval of this Common.

        HLS分片间隔，仅封装类型“pack_type”取值为1或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 

        :param hls_interval: The hls_interval of this Common.
        :type hls_interval: int
        """
        self._hls_interval = hls_interval

    @property
    def dash_interval(self):
        """Gets the dash_interval of this Common.

        DASH间隔，仅封装类型“pack_type”取值为2或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 

        :return: The dash_interval of this Common.
        :rtype: int
        """
        return self._dash_interval

    @dash_interval.setter
    def dash_interval(self, dash_interval):
        """Sets the dash_interval of this Common.

        DASH间隔，仅封装类型“pack_type”取值为2或3时，该参数生效。  取值范围：[2，10]。  单位：秒。 

        :param dash_interval: The dash_interval of this Common.
        :type dash_interval: int
        """
        self._dash_interval = dash_interval

    @property
    def pack_type(self):
        """Gets the pack_type of this Common.

        封装类型。  取值如下： - 1：HLS - 2：DASH - 3：HLS+DASH - 4：MP4 - 5：MP3 - 6：ADTS  > pack_type设置为5和6时，不能设置视频参数。 

        :return: The pack_type of this Common.
        :rtype: int
        """
        return self._pack_type

    @pack_type.setter
    def pack_type(self, pack_type):
        """Sets the pack_type of this Common.

        封装类型。  取值如下： - 1：HLS - 2：DASH - 3：HLS+DASH - 4：MP4 - 5：MP3 - 6：ADTS  > pack_type设置为5和6时，不能设置视频参数。 

        :param pack_type: The pack_type of this Common.
        :type pack_type: int
        """
        self._pack_type = pack_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Common):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
