# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Compliance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkitem_id': 'str',
        'checkpoint_id': 'str',
        'spec_id': 'str',
        'status': 'str',
        'properties': 'str'
    }

    attribute_map = {
        'checkitem_id': 'checkitem_id',
        'checkpoint_id': 'checkpoint_id',
        'spec_id': 'spec_id',
        'status': 'status',
        'properties': 'properties'
    }

    def __init__(self, checkitem_id=None, checkpoint_id=None, spec_id=None, status=None, properties=None):
        r"""Compliance

        The model defined in huaweicloud sdk

        :param checkitem_id: 检查项（检查规则）编号
        :type checkitem_id: str
        :param checkpoint_id: 检查点（检查结果）编号，检查项对同一个资源的检查结果
        :type checkpoint_id: str
        :param spec_id: 检查规范编号，默认选第一个
        :type spec_id: str
        :param status: 合规检查结果，取值定义：PASSED、WARNING、FAILED、NOT_AVAILABLE。 说明： PASSED - 接受评估的所有资源都已通过安全检查。 WARNING - 某些信息缺失或配置不支持此检查。 FAILED - 至少有一个接受评估的资源未能通过安全检查。 NOT_AVAILABLE - 由于服务中断或 API 错误，无法执行检查。
        :type status: str
        :param properties: 属性信息
        :type properties: str
        """
        
        

        self._checkitem_id = None
        self._checkpoint_id = None
        self._spec_id = None
        self._status = None
        self._properties = None
        self.discriminator = None

        self.checkitem_id = checkitem_id
        self.checkpoint_id = checkpoint_id
        self.spec_id = spec_id
        self.status = status
        if properties is not None:
            self.properties = properties

    @property
    def checkitem_id(self):
        r"""Gets the checkitem_id of this Compliance.

        检查项（检查规则）编号

        :return: The checkitem_id of this Compliance.
        :rtype: str
        """
        return self._checkitem_id

    @checkitem_id.setter
    def checkitem_id(self, checkitem_id):
        r"""Sets the checkitem_id of this Compliance.

        检查项（检查规则）编号

        :param checkitem_id: The checkitem_id of this Compliance.
        :type checkitem_id: str
        """
        self._checkitem_id = checkitem_id

    @property
    def checkpoint_id(self):
        r"""Gets the checkpoint_id of this Compliance.

        检查点（检查结果）编号，检查项对同一个资源的检查结果

        :return: The checkpoint_id of this Compliance.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        r"""Sets the checkpoint_id of this Compliance.

        检查点（检查结果）编号，检查项对同一个资源的检查结果

        :param checkpoint_id: The checkpoint_id of this Compliance.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def spec_id(self):
        r"""Gets the spec_id of this Compliance.

        检查规范编号，默认选第一个

        :return: The spec_id of this Compliance.
        :rtype: str
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        r"""Sets the spec_id of this Compliance.

        检查规范编号，默认选第一个

        :param spec_id: The spec_id of this Compliance.
        :type spec_id: str
        """
        self._spec_id = spec_id

    @property
    def status(self):
        r"""Gets the status of this Compliance.

        合规检查结果，取值定义：PASSED、WARNING、FAILED、NOT_AVAILABLE。 说明： PASSED - 接受评估的所有资源都已通过安全检查。 WARNING - 某些信息缺失或配置不支持此检查。 FAILED - 至少有一个接受评估的资源未能通过安全检查。 NOT_AVAILABLE - 由于服务中断或 API 错误，无法执行检查。

        :return: The status of this Compliance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Compliance.

        合规检查结果，取值定义：PASSED、WARNING、FAILED、NOT_AVAILABLE。 说明： PASSED - 接受评估的所有资源都已通过安全检查。 WARNING - 某些信息缺失或配置不支持此检查。 FAILED - 至少有一个接受评估的资源未能通过安全检查。 NOT_AVAILABLE - 由于服务中断或 API 错误，无法执行检查。

        :param status: The status of this Compliance.
        :type status: str
        """
        self._status = status

    @property
    def properties(self):
        r"""Gets the properties of this Compliance.

        属性信息

        :return: The properties of this Compliance.
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this Compliance.

        属性信息

        :param properties: The properties of this Compliance.
        :type properties: str
        """
        self._properties = properties

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
        if not isinstance(other, Compliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
