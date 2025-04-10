# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesClientClientTypeOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sc_type_window': 'bool',
        'sc_type_mac': 'bool',
        'sc_type_android': 'bool',
        'sc_type_linux': 'bool',
        'sc_type_h5': 'bool',
        'sc_type_ios': 'bool',
        'sc_type_harmony_os': 'bool',
        'tc_type_all': 'bool'
    }

    attribute_map = {
        'sc_type_window': 'sc_type_window',
        'sc_type_mac': 'sc_type_mac',
        'sc_type_android': 'sc_type_android',
        'sc_type_linux': 'sc_type_linux',
        'sc_type_h5': 'sc_type_h5',
        'sc_type_ios': 'sc_type_ios',
        'sc_type_harmony_os': 'sc_type_harmony_os',
        'tc_type_all': 'tc_type_all'
    }

    def __init__(self, sc_type_window=None, sc_type_mac=None, sc_type_android=None, sc_type_linux=None, sc_type_h5=None, sc_type_ios=None, sc_type_harmony_os=None, tc_type_all=None):
        r"""PoliciesClientClientTypeOptions

        The model defined in huaweicloud sdk

        :param sc_type_window: 是否勾选Windows客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_window: bool
        :param sc_type_mac: 是否勾选macOS客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_mac: bool
        :param sc_type_android: 是否勾选Android客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_android: bool
        :param sc_type_linux: 是否勾选Linux客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_linux: bool
        :param sc_type_h5: 是否勾选Web客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_h5: bool
        :param sc_type_ios: 是否勾选ios客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_ios: bool
        :param sc_type_harmony_os: 是否勾选鸿蒙客户端。取值为： false：表示未勾选。 true：表示勾选。
        :type sc_type_harmony_os: bool
        :param tc_type_all: 是否勾选全部硬件终端。取值为： false：表示未勾选。 true：表示勾选。
        :type tc_type_all: bool
        """
        
        

        self._sc_type_window = None
        self._sc_type_mac = None
        self._sc_type_android = None
        self._sc_type_linux = None
        self._sc_type_h5 = None
        self._sc_type_ios = None
        self._sc_type_harmony_os = None
        self._tc_type_all = None
        self.discriminator = None

        if sc_type_window is not None:
            self.sc_type_window = sc_type_window
        if sc_type_mac is not None:
            self.sc_type_mac = sc_type_mac
        if sc_type_android is not None:
            self.sc_type_android = sc_type_android
        if sc_type_linux is not None:
            self.sc_type_linux = sc_type_linux
        if sc_type_h5 is not None:
            self.sc_type_h5 = sc_type_h5
        if sc_type_ios is not None:
            self.sc_type_ios = sc_type_ios
        if sc_type_harmony_os is not None:
            self.sc_type_harmony_os = sc_type_harmony_os
        if tc_type_all is not None:
            self.tc_type_all = tc_type_all

    @property
    def sc_type_window(self):
        r"""Gets the sc_type_window of this PoliciesClientClientTypeOptions.

        是否勾选Windows客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_window of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_window

    @sc_type_window.setter
    def sc_type_window(self, sc_type_window):
        r"""Sets the sc_type_window of this PoliciesClientClientTypeOptions.

        是否勾选Windows客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_window: The sc_type_window of this PoliciesClientClientTypeOptions.
        :type sc_type_window: bool
        """
        self._sc_type_window = sc_type_window

    @property
    def sc_type_mac(self):
        r"""Gets the sc_type_mac of this PoliciesClientClientTypeOptions.

        是否勾选macOS客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_mac of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_mac

    @sc_type_mac.setter
    def sc_type_mac(self, sc_type_mac):
        r"""Sets the sc_type_mac of this PoliciesClientClientTypeOptions.

        是否勾选macOS客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_mac: The sc_type_mac of this PoliciesClientClientTypeOptions.
        :type sc_type_mac: bool
        """
        self._sc_type_mac = sc_type_mac

    @property
    def sc_type_android(self):
        r"""Gets the sc_type_android of this PoliciesClientClientTypeOptions.

        是否勾选Android客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_android of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_android

    @sc_type_android.setter
    def sc_type_android(self, sc_type_android):
        r"""Sets the sc_type_android of this PoliciesClientClientTypeOptions.

        是否勾选Android客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_android: The sc_type_android of this PoliciesClientClientTypeOptions.
        :type sc_type_android: bool
        """
        self._sc_type_android = sc_type_android

    @property
    def sc_type_linux(self):
        r"""Gets the sc_type_linux of this PoliciesClientClientTypeOptions.

        是否勾选Linux客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_linux of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_linux

    @sc_type_linux.setter
    def sc_type_linux(self, sc_type_linux):
        r"""Sets the sc_type_linux of this PoliciesClientClientTypeOptions.

        是否勾选Linux客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_linux: The sc_type_linux of this PoliciesClientClientTypeOptions.
        :type sc_type_linux: bool
        """
        self._sc_type_linux = sc_type_linux

    @property
    def sc_type_h5(self):
        r"""Gets the sc_type_h5 of this PoliciesClientClientTypeOptions.

        是否勾选Web客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_h5 of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_h5

    @sc_type_h5.setter
    def sc_type_h5(self, sc_type_h5):
        r"""Sets the sc_type_h5 of this PoliciesClientClientTypeOptions.

        是否勾选Web客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_h5: The sc_type_h5 of this PoliciesClientClientTypeOptions.
        :type sc_type_h5: bool
        """
        self._sc_type_h5 = sc_type_h5

    @property
    def sc_type_ios(self):
        r"""Gets the sc_type_ios of this PoliciesClientClientTypeOptions.

        是否勾选ios客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_ios of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_ios

    @sc_type_ios.setter
    def sc_type_ios(self, sc_type_ios):
        r"""Sets the sc_type_ios of this PoliciesClientClientTypeOptions.

        是否勾选ios客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_ios: The sc_type_ios of this PoliciesClientClientTypeOptions.
        :type sc_type_ios: bool
        """
        self._sc_type_ios = sc_type_ios

    @property
    def sc_type_harmony_os(self):
        r"""Gets the sc_type_harmony_os of this PoliciesClientClientTypeOptions.

        是否勾选鸿蒙客户端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The sc_type_harmony_os of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._sc_type_harmony_os

    @sc_type_harmony_os.setter
    def sc_type_harmony_os(self, sc_type_harmony_os):
        r"""Sets the sc_type_harmony_os of this PoliciesClientClientTypeOptions.

        是否勾选鸿蒙客户端。取值为： false：表示未勾选。 true：表示勾选。

        :param sc_type_harmony_os: The sc_type_harmony_os of this PoliciesClientClientTypeOptions.
        :type sc_type_harmony_os: bool
        """
        self._sc_type_harmony_os = sc_type_harmony_os

    @property
    def tc_type_all(self):
        r"""Gets the tc_type_all of this PoliciesClientClientTypeOptions.

        是否勾选全部硬件终端。取值为： false：表示未勾选。 true：表示勾选。

        :return: The tc_type_all of this PoliciesClientClientTypeOptions.
        :rtype: bool
        """
        return self._tc_type_all

    @tc_type_all.setter
    def tc_type_all(self, tc_type_all):
        r"""Sets the tc_type_all of this PoliciesClientClientTypeOptions.

        是否勾选全部硬件终端。取值为： false：表示未勾选。 true：表示勾选。

        :param tc_type_all: The tc_type_all of this PoliciesClientClientTypeOptions.
        :type tc_type_all: bool
        """
        self._tc_type_all = tc_type_all

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
        if not isinstance(other, PoliciesClientClientTypeOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
