# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSystemUserWhiteListRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'system_user_name_list': 'list[str]',
        'remarks': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'system_user_name_list': 'system_user_name_list',
        'remarks': 'remarks'
    }

    def __init__(self, host_id=None, system_user_name_list=None, remarks=None):
        r"""AddSystemUserWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param system_user_name_list: 系统用户名列表
        :type system_user_name_list: list[str]
        :param remarks: 备注
        :type remarks: str
        """
        
        

        self._host_id = None
        self._system_user_name_list = None
        self._remarks = None
        self.discriminator = None

        self.host_id = host_id
        self.system_user_name_list = system_user_name_list
        if remarks is not None:
            self.remarks = remarks

    @property
    def host_id(self):
        r"""Gets the host_id of this AddSystemUserWhiteListRequestInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AddSystemUserWhiteListRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AddSystemUserWhiteListRequestInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AddSystemUserWhiteListRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def system_user_name_list(self):
        r"""Gets the system_user_name_list of this AddSystemUserWhiteListRequestInfo.

        系统用户名列表

        :return: The system_user_name_list of this AddSystemUserWhiteListRequestInfo.
        :rtype: list[str]
        """
        return self._system_user_name_list

    @system_user_name_list.setter
    def system_user_name_list(self, system_user_name_list):
        r"""Sets the system_user_name_list of this AddSystemUserWhiteListRequestInfo.

        系统用户名列表

        :param system_user_name_list: The system_user_name_list of this AddSystemUserWhiteListRequestInfo.
        :type system_user_name_list: list[str]
        """
        self._system_user_name_list = system_user_name_list

    @property
    def remarks(self):
        r"""Gets the remarks of this AddSystemUserWhiteListRequestInfo.

        备注

        :return: The remarks of this AddSystemUserWhiteListRequestInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this AddSystemUserWhiteListRequestInfo.

        备注

        :param remarks: The remarks of this AddSystemUserWhiteListRequestInfo.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, AddSystemUserWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
