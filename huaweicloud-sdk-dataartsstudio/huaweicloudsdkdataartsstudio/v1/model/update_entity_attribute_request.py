# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEntityAttributeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'guid': 'str',
        'attr_name': 'str',
        'attr_value': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid',
        'attr_name': 'attr_name',
        'attr_value': 'attr_value'
    }

    def __init__(self, workspace=None, guid=None, attr_name=None, attr_value=None):
        r"""UpdateEntityAttributeRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param guid: 资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。
        :type guid: str
        :param attr_name: 要修改的属性名称，如description、alias、comment等。
        :type attr_name: str
        :param attr_value: 要修改的属性值。
        :type attr_value: str
        """
        
        

        self._workspace = None
        self._guid = None
        self._attr_name = None
        self._attr_value = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid
        self.attr_name = attr_name
        self.attr_value = attr_value

    @property
    def workspace(self):
        r"""Gets the workspace of this UpdateEntityAttributeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this UpdateEntityAttributeRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this UpdateEntityAttributeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this UpdateEntityAttributeRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        r"""Gets the guid of this UpdateEntityAttributeRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :return: The guid of this UpdateEntityAttributeRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this UpdateEntityAttributeRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :param guid: The guid of this UpdateEntityAttributeRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def attr_name(self):
        r"""Gets the attr_name of this UpdateEntityAttributeRequest.

        要修改的属性名称，如description、alias、comment等。

        :return: The attr_name of this UpdateEntityAttributeRequest.
        :rtype: str
        """
        return self._attr_name

    @attr_name.setter
    def attr_name(self, attr_name):
        r"""Sets the attr_name of this UpdateEntityAttributeRequest.

        要修改的属性名称，如description、alias、comment等。

        :param attr_name: The attr_name of this UpdateEntityAttributeRequest.
        :type attr_name: str
        """
        self._attr_name = attr_name

    @property
    def attr_value(self):
        r"""Gets the attr_value of this UpdateEntityAttributeRequest.

        要修改的属性值。

        :return: The attr_value of this UpdateEntityAttributeRequest.
        :rtype: str
        """
        return self._attr_value

    @attr_value.setter
    def attr_value(self, attr_value):
        r"""Sets the attr_value of this UpdateEntityAttributeRequest.

        要修改的属性值。

        :param attr_value: The attr_value of this UpdateEntityAttributeRequest.
        :type attr_value: str
        """
        self._attr_value = attr_value

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
        if not isinstance(other, UpdateEntityAttributeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
