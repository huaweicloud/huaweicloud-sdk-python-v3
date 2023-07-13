# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostGroupResponse(SdkResponse):

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
        'host_group_type': 'str',
        'host_id_list': 'list[str]',
        'host_group_tag': 'list[HostGroupTag]',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'host_group_id': 'host_group_id',
        'host_group_name': 'host_group_name',
        'host_group_type': 'host_group_type',
        'host_id_list': 'host_id_list',
        'host_group_tag': 'host_group_tag',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, host_group_id=None, host_group_name=None, host_group_type=None, host_id_list=None, host_group_tag=None, create_time=None, update_time=None):
        """UpdateHostGroupResponse

        The model defined in huaweicloud sdk

        :param host_group_id: 主机组ID
        :type host_group_id: str
        :param host_group_name: 主机组名称
        :type host_group_name: str
        :param host_group_type: 主机组类型。linux：linux类型，windows：windows类型
        :type host_group_type: str
        :param host_id_list: 主机ID列表
        :type host_id_list: list[str]
        :param host_group_tag: 标签信息
        :type host_group_tag: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super(UpdateHostGroupResponse, self).__init__()

        self._host_group_id = None
        self._host_group_name = None
        self._host_group_type = None
        self._host_id_list = None
        self._host_group_tag = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if host_group_id is not None:
            self.host_group_id = host_group_id
        if host_group_name is not None:
            self.host_group_name = host_group_name
        if host_group_type is not None:
            self.host_group_type = host_group_type
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if host_group_tag is not None:
            self.host_group_tag = host_group_tag
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def host_group_id(self):
        """Gets the host_group_id of this UpdateHostGroupResponse.

        主机组ID

        :return: The host_group_id of this UpdateHostGroupResponse.
        :rtype: str
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        """Sets the host_group_id of this UpdateHostGroupResponse.

        主机组ID

        :param host_group_id: The host_group_id of this UpdateHostGroupResponse.
        :type host_group_id: str
        """
        self._host_group_id = host_group_id

    @property
    def host_group_name(self):
        """Gets the host_group_name of this UpdateHostGroupResponse.

        主机组名称

        :return: The host_group_name of this UpdateHostGroupResponse.
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        """Sets the host_group_name of this UpdateHostGroupResponse.

        主机组名称

        :param host_group_name: The host_group_name of this UpdateHostGroupResponse.
        :type host_group_name: str
        """
        self._host_group_name = host_group_name

    @property
    def host_group_type(self):
        """Gets the host_group_type of this UpdateHostGroupResponse.

        主机组类型。linux：linux类型，windows：windows类型

        :return: The host_group_type of this UpdateHostGroupResponse.
        :rtype: str
        """
        return self._host_group_type

    @host_group_type.setter
    def host_group_type(self, host_group_type):
        """Sets the host_group_type of this UpdateHostGroupResponse.

        主机组类型。linux：linux类型，windows：windows类型

        :param host_group_type: The host_group_type of this UpdateHostGroupResponse.
        :type host_group_type: str
        """
        self._host_group_type = host_group_type

    @property
    def host_id_list(self):
        """Gets the host_id_list of this UpdateHostGroupResponse.

        主机ID列表

        :return: The host_id_list of this UpdateHostGroupResponse.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this UpdateHostGroupResponse.

        主机ID列表

        :param host_id_list: The host_id_list of this UpdateHostGroupResponse.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def host_group_tag(self):
        """Gets the host_group_tag of this UpdateHostGroupResponse.

        标签信息

        :return: The host_group_tag of this UpdateHostGroupResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        return self._host_group_tag

    @host_group_tag.setter
    def host_group_tag(self, host_group_tag):
        """Sets the host_group_tag of this UpdateHostGroupResponse.

        标签信息

        :param host_group_tag: The host_group_tag of this UpdateHostGroupResponse.
        :type host_group_tag: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        self._host_group_tag = host_group_tag

    @property
    def create_time(self):
        """Gets the create_time of this UpdateHostGroupResponse.

        创建时间

        :return: The create_time of this UpdateHostGroupResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateHostGroupResponse.

        创建时间

        :param create_time: The create_time of this UpdateHostGroupResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateHostGroupResponse.

        更新时间

        :return: The update_time of this UpdateHostGroupResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateHostGroupResponse.

        更新时间

        :param update_time: The update_time of this UpdateHostGroupResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateHostGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
