# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_group_id': 'str',
        'host_group_name': 'str',
        'host_id_list': 'list[str]',
        'host_group_tag': 'list[HostGroupTag]'
    }

    attribute_map = {
        'host_group_id': 'host_group_id',
        'host_group_name': 'host_group_name',
        'host_id_list': 'host_id_list',
        'host_group_tag': 'host_group_tag'
    }

    def __init__(self, host_group_id=None, host_group_name=None, host_id_list=None, host_group_tag=None):
        r"""UpdateHostGroupRequestBody

        The model defined in huaweicloud sdk

        :param host_group_id: 主机组ID
        :type host_group_id: str
        :param host_group_name: 主机组名称
        :type host_group_name: str
        :param host_id_list: 主机ID列表。主机类型必须与主机组类型一致
        :type host_id_list: list[str]
        :param host_group_tag: 主机组标签。KEY不能重复
        :type host_group_tag: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        
        

        self._host_group_id = None
        self._host_group_name = None
        self._host_id_list = None
        self._host_group_tag = None
        self.discriminator = None

        self.host_group_id = host_group_id
        if host_group_name is not None:
            self.host_group_name = host_group_name
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if host_group_tag is not None:
            self.host_group_tag = host_group_tag

    @property
    def host_group_id(self):
        r"""Gets the host_group_id of this UpdateHostGroupRequestBody.

        主机组ID

        :return: The host_group_id of this UpdateHostGroupRequestBody.
        :rtype: str
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        r"""Sets the host_group_id of this UpdateHostGroupRequestBody.

        主机组ID

        :param host_group_id: The host_group_id of this UpdateHostGroupRequestBody.
        :type host_group_id: str
        """
        self._host_group_id = host_group_id

    @property
    def host_group_name(self):
        r"""Gets the host_group_name of this UpdateHostGroupRequestBody.

        主机组名称

        :return: The host_group_name of this UpdateHostGroupRequestBody.
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        r"""Sets the host_group_name of this UpdateHostGroupRequestBody.

        主机组名称

        :param host_group_name: The host_group_name of this UpdateHostGroupRequestBody.
        :type host_group_name: str
        """
        self._host_group_name = host_group_name

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this UpdateHostGroupRequestBody.

        主机ID列表。主机类型必须与主机组类型一致

        :return: The host_id_list of this UpdateHostGroupRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this UpdateHostGroupRequestBody.

        主机ID列表。主机类型必须与主机组类型一致

        :param host_id_list: The host_id_list of this UpdateHostGroupRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def host_group_tag(self):
        r"""Gets the host_group_tag of this UpdateHostGroupRequestBody.

        主机组标签。KEY不能重复

        :return: The host_group_tag of this UpdateHostGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        return self._host_group_tag

    @host_group_tag.setter
    def host_group_tag(self, host_group_tag):
        r"""Sets the host_group_tag of this UpdateHostGroupRequestBody.

        主机组标签。KEY不能重复

        :param host_group_tag: The host_group_tag of this UpdateHostGroupRequestBody.
        :type host_group_tag: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
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
        if not isinstance(other, UpdateHostGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
