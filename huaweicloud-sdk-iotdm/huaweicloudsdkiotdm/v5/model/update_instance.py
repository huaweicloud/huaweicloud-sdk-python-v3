# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'operate_window': 'OperateWindow',
        'forwarding_info': 'UpdateForwardingInfo',
        'access_info': 'UpdateAccessInfo'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'operate_window': 'operate_window',
        'forwarding_info': 'forwarding_info',
        'access_info': 'access_info'
    }

    def __init__(self, name=None, description=None, operate_window=None, forwarding_info=None, access_info=None):
        r"""UpdateInstance

        The model defined in huaweicloud sdk

        :param name: **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 
        :type name: str
        :param description: **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 
        :type description: str
        :param operate_window: 
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        :param forwarding_info: 
        :type forwarding_info: :class:`huaweicloudsdkiotdm.v5.UpdateForwardingInfo`
        :param access_info: 
        :type access_info: :class:`huaweicloudsdkiotdm.v5.UpdateAccessInfo`
        """
        
        

        self._name = None
        self._description = None
        self._operate_window = None
        self._forwarding_info = None
        self._access_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if operate_window is not None:
            self.operate_window = operate_window
        if forwarding_info is not None:
            self.forwarding_info = forwarding_info
        if access_info is not None:
            self.access_info = access_info

    @property
    def name(self):
        r"""Gets the name of this UpdateInstance.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :return: The name of this UpdateInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInstance.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :param name: The name of this UpdateInstance.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateInstance.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :return: The description of this UpdateInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInstance.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :param description: The description of this UpdateInstance.
        :type description: str
        """
        self._description = description

    @property
    def operate_window(self):
        r"""Gets the operate_window of this UpdateInstance.

        :return: The operate_window of this UpdateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        return self._operate_window

    @operate_window.setter
    def operate_window(self, operate_window):
        r"""Sets the operate_window of this UpdateInstance.

        :param operate_window: The operate_window of this UpdateInstance.
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        self._operate_window = operate_window

    @property
    def forwarding_info(self):
        r"""Gets the forwarding_info of this UpdateInstance.

        :return: The forwarding_info of this UpdateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.UpdateForwardingInfo`
        """
        return self._forwarding_info

    @forwarding_info.setter
    def forwarding_info(self, forwarding_info):
        r"""Sets the forwarding_info of this UpdateInstance.

        :param forwarding_info: The forwarding_info of this UpdateInstance.
        :type forwarding_info: :class:`huaweicloudsdkiotdm.v5.UpdateForwardingInfo`
        """
        self._forwarding_info = forwarding_info

    @property
    def access_info(self):
        r"""Gets the access_info of this UpdateInstance.

        :return: The access_info of this UpdateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.UpdateAccessInfo`
        """
        return self._access_info

    @access_info.setter
    def access_info(self, access_info):
        r"""Sets the access_info of this UpdateInstance.

        :param access_info: The access_info of this UpdateInstance.
        :type access_info: :class:`huaweicloudsdkiotdm.v5.UpdateAccessInfo`
        """
        self._access_info = access_info

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
        if not isinstance(other, UpdateInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
