# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHostGroupListFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_group_type': 'str',
        'host_group_name_list': 'list[str]',
        'host_name_list': 'list[str]',
        'host_group_tag': 'GetHostGroupListTag'
    }

    attribute_map = {
        'host_group_type': 'host_group_type',
        'host_group_name_list': 'host_group_name_list',
        'host_name_list': 'host_name_list',
        'host_group_tag': 'host_group_tag'
    }

    def __init__(self, host_group_type=None, host_group_name_list=None, host_name_list=None, host_group_tag=None):
        r"""GetHostGroupListFilter

        The model defined in huaweicloud sdk

        :param host_group_type: 主机组类型。windows：windows类型，linux：linux类型
        :type host_group_type: str
        :param host_group_name_list: 主机组名称列表。
        :type host_group_name_list: list[str]
        :param host_name_list: 主机名称列表。
        :type host_name_list: list[str]
        :param host_group_tag: 
        :type host_group_tag: :class:`huaweicloudsdklts.v2.GetHostGroupListTag`
        """
        
        

        self._host_group_type = None
        self._host_group_name_list = None
        self._host_name_list = None
        self._host_group_tag = None
        self.discriminator = None

        if host_group_type is not None:
            self.host_group_type = host_group_type
        if host_group_name_list is not None:
            self.host_group_name_list = host_group_name_list
        if host_name_list is not None:
            self.host_name_list = host_name_list
        if host_group_tag is not None:
            self.host_group_tag = host_group_tag

    @property
    def host_group_type(self):
        r"""Gets the host_group_type of this GetHostGroupListFilter.

        主机组类型。windows：windows类型，linux：linux类型

        :return: The host_group_type of this GetHostGroupListFilter.
        :rtype: str
        """
        return self._host_group_type

    @host_group_type.setter
    def host_group_type(self, host_group_type):
        r"""Sets the host_group_type of this GetHostGroupListFilter.

        主机组类型。windows：windows类型，linux：linux类型

        :param host_group_type: The host_group_type of this GetHostGroupListFilter.
        :type host_group_type: str
        """
        self._host_group_type = host_group_type

    @property
    def host_group_name_list(self):
        r"""Gets the host_group_name_list of this GetHostGroupListFilter.

        主机组名称列表。

        :return: The host_group_name_list of this GetHostGroupListFilter.
        :rtype: list[str]
        """
        return self._host_group_name_list

    @host_group_name_list.setter
    def host_group_name_list(self, host_group_name_list):
        r"""Sets the host_group_name_list of this GetHostGroupListFilter.

        主机组名称列表。

        :param host_group_name_list: The host_group_name_list of this GetHostGroupListFilter.
        :type host_group_name_list: list[str]
        """
        self._host_group_name_list = host_group_name_list

    @property
    def host_name_list(self):
        r"""Gets the host_name_list of this GetHostGroupListFilter.

        主机名称列表。

        :return: The host_name_list of this GetHostGroupListFilter.
        :rtype: list[str]
        """
        return self._host_name_list

    @host_name_list.setter
    def host_name_list(self, host_name_list):
        r"""Sets the host_name_list of this GetHostGroupListFilter.

        主机名称列表。

        :param host_name_list: The host_name_list of this GetHostGroupListFilter.
        :type host_name_list: list[str]
        """
        self._host_name_list = host_name_list

    @property
    def host_group_tag(self):
        r"""Gets the host_group_tag of this GetHostGroupListFilter.

        :return: The host_group_tag of this GetHostGroupListFilter.
        :rtype: :class:`huaweicloudsdklts.v2.GetHostGroupListTag`
        """
        return self._host_group_tag

    @host_group_tag.setter
    def host_group_tag(self, host_group_tag):
        r"""Sets the host_group_tag of this GetHostGroupListFilter.

        :param host_group_tag: The host_group_tag of this GetHostGroupListFilter.
        :type host_group_tag: :class:`huaweicloudsdklts.v2.GetHostGroupListTag`
        """
        self._host_group_tag = host_group_tag

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
        if not isinstance(other, GetHostGroupListFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
