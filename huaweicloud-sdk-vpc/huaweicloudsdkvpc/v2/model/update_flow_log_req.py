# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlowLogReq:

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
        'admin_state': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'admin_state': 'admin_state'
    }

    def __init__(self, name=None, description=None, admin_state=None):
        """UpdateFlowLogReq

        The model defined in huaweicloud sdk

        :param name: 功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：流日志描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param admin_state: 功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志。
        :type admin_state: bool
        """
        
        

        self._name = None
        self._description = None
        self._admin_state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state is not None:
            self.admin_state = admin_state

    @property
    def name(self):
        """Gets the name of this UpdateFlowLogReq.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :return: The name of this UpdateFlowLogReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateFlowLogReq.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :param name: The name of this UpdateFlowLogReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateFlowLogReq.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this UpdateFlowLogReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFlowLogReq.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this UpdateFlowLogReq.
        :type description: str
        """
        self._description = description

    @property
    def admin_state(self):
        """Gets the admin_state of this UpdateFlowLogReq.

        功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志。

        :return: The admin_state of this UpdateFlowLogReq.
        :rtype: bool
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this UpdateFlowLogReq.

        功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志。

        :param admin_state: The admin_state of this UpdateFlowLogReq.
        :type admin_state: bool
        """
        self._admin_state = admin_state

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
        if not isinstance(other, UpdateFlowLogReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
