# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVmrResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vmr_id': 'str',
        'vmr_name': 'str',
        'gust_pwd': 'str',
        'gust_join_url': 'str',
        'chair_pwd': 'str',
        'chair_join_url': 'str',
        'allow_gust_first': 'bool',
        'gust_first_notice': 'bool',
        'vmr_mode': 'int',
        'vmr_pkg_id': 'str',
        'vmr_pkg_name': 'str',
        'vmr_pkg_parties': 'int',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vmr_id': 'vmrId',
        'vmr_name': 'vmrName',
        'gust_pwd': 'gustPwd',
        'gust_join_url': 'gustJoinUrl',
        'chair_pwd': 'chairPwd',
        'chair_join_url': 'chairJoinUrl',
        'allow_gust_first': 'allowGustFirst',
        'gust_first_notice': 'gustFirstNotice',
        'vmr_mode': 'vmrMode',
        'vmr_pkg_id': 'vmrPkgId',
        'vmr_pkg_name': 'vmrPkgName',
        'vmr_pkg_parties': 'vmrPkgParties',
        'status': 'status'
    }

    def __init__(self, id=None, vmr_id=None, vmr_name=None, gust_pwd=None, gust_join_url=None, chair_pwd=None, chair_join_url=None, allow_gust_first=None, gust_first_notice=None, vmr_mode=None, vmr_pkg_id=None, vmr_pkg_name=None, vmr_pkg_parties=None, status=None):
        """QueryVmrResultDTO

        The model defined in huaweicloud sdk

        :param id: 云会议室的ID。 &gt; 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 
        :type id: str
        :param vmr_id: 云会议室的固定会议ID或者个人会议ID。 &gt; 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 
        :type vmr_id: str
        :param vmr_name: 云会议室名称。
        :type vmr_name: str
        :param gust_pwd: 来宾密码。
        :type gust_pwd: str
        :param gust_join_url: 来宾与会链接。
        :type gust_join_url: str
        :param chair_pwd: 主持人密码。
        :type chair_pwd: str
        :param chair_join_url: 主持人与会链接。
        :type chair_join_url: str
        :param allow_gust_first: 允许来宾先入会。
        :type allow_gust_first: bool
        :param gust_first_notice: 云会议室被使用后是否通知会议室所有者。
        :type gust_first_notice: bool
        :param vmr_mode: VMR模式。 * 0: 个人会议ID * 1: 云会议室 * 2: 网络研讨会 
        :type vmr_mode: int
        :param vmr_pkg_id: 云会议室套餐包的id，仅云会议室返回。
        :type vmr_pkg_id: str
        :param vmr_pkg_name: 云会议室套餐包的名称，仅云会议室返回。
        :type vmr_pkg_name: str
        :param vmr_pkg_parties: 云会议室套餐包的会议并发方数，仅云会议室返回。
        :type vmr_pkg_parties: int
        :param status: 云会议室状态。 * 0：正常 * 1：停用 * 2：未分配 
        :type status: int
        """
        
        

        self._id = None
        self._vmr_id = None
        self._vmr_name = None
        self._gust_pwd = None
        self._gust_join_url = None
        self._chair_pwd = None
        self._chair_join_url = None
        self._allow_gust_first = None
        self._gust_first_notice = None
        self._vmr_mode = None
        self._vmr_pkg_id = None
        self._vmr_pkg_name = None
        self._vmr_pkg_parties = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if gust_pwd is not None:
            self.gust_pwd = gust_pwd
        if gust_join_url is not None:
            self.gust_join_url = gust_join_url
        if chair_pwd is not None:
            self.chair_pwd = chair_pwd
        if chair_join_url is not None:
            self.chair_join_url = chair_join_url
        if allow_gust_first is not None:
            self.allow_gust_first = allow_gust_first
        if gust_first_notice is not None:
            self.gust_first_notice = gust_first_notice
        if vmr_mode is not None:
            self.vmr_mode = vmr_mode
        if vmr_pkg_id is not None:
            self.vmr_pkg_id = vmr_pkg_id
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
        if vmr_pkg_parties is not None:
            self.vmr_pkg_parties = vmr_pkg_parties
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this QueryVmrResultDTO.

        云会议室的ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 

        :return: The id of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryVmrResultDTO.

        云会议室的ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 

        :param id: The id of this QueryVmrResultDTO.
        :type id: str
        """
        self._id = id

    @property
    def vmr_id(self):
        """Gets the vmr_id of this QueryVmrResultDTO.

        云会议室的固定会议ID或者个人会议ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 

        :return: The vmr_id of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this QueryVmrResultDTO.

        云会议室的固定会议ID或者个人会议ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 

        :param vmr_id: The vmr_id of this QueryVmrResultDTO.
        :type vmr_id: str
        """
        self._vmr_id = vmr_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this QueryVmrResultDTO.

        云会议室名称。

        :return: The vmr_name of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this QueryVmrResultDTO.

        云会议室名称。

        :param vmr_name: The vmr_name of this QueryVmrResultDTO.
        :type vmr_name: str
        """
        self._vmr_name = vmr_name

    @property
    def gust_pwd(self):
        """Gets the gust_pwd of this QueryVmrResultDTO.

        来宾密码。

        :return: The gust_pwd of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._gust_pwd

    @gust_pwd.setter
    def gust_pwd(self, gust_pwd):
        """Sets the gust_pwd of this QueryVmrResultDTO.

        来宾密码。

        :param gust_pwd: The gust_pwd of this QueryVmrResultDTO.
        :type gust_pwd: str
        """
        self._gust_pwd = gust_pwd

    @property
    def gust_join_url(self):
        """Gets the gust_join_url of this QueryVmrResultDTO.

        来宾与会链接。

        :return: The gust_join_url of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._gust_join_url

    @gust_join_url.setter
    def gust_join_url(self, gust_join_url):
        """Sets the gust_join_url of this QueryVmrResultDTO.

        来宾与会链接。

        :param gust_join_url: The gust_join_url of this QueryVmrResultDTO.
        :type gust_join_url: str
        """
        self._gust_join_url = gust_join_url

    @property
    def chair_pwd(self):
        """Gets the chair_pwd of this QueryVmrResultDTO.

        主持人密码。

        :return: The chair_pwd of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._chair_pwd

    @chair_pwd.setter
    def chair_pwd(self, chair_pwd):
        """Sets the chair_pwd of this QueryVmrResultDTO.

        主持人密码。

        :param chair_pwd: The chair_pwd of this QueryVmrResultDTO.
        :type chair_pwd: str
        """
        self._chair_pwd = chair_pwd

    @property
    def chair_join_url(self):
        """Gets the chair_join_url of this QueryVmrResultDTO.

        主持人与会链接。

        :return: The chair_join_url of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._chair_join_url

    @chair_join_url.setter
    def chair_join_url(self, chair_join_url):
        """Sets the chair_join_url of this QueryVmrResultDTO.

        主持人与会链接。

        :param chair_join_url: The chair_join_url of this QueryVmrResultDTO.
        :type chair_join_url: str
        """
        self._chair_join_url = chair_join_url

    @property
    def allow_gust_first(self):
        """Gets the allow_gust_first of this QueryVmrResultDTO.

        允许来宾先入会。

        :return: The allow_gust_first of this QueryVmrResultDTO.
        :rtype: bool
        """
        return self._allow_gust_first

    @allow_gust_first.setter
    def allow_gust_first(self, allow_gust_first):
        """Sets the allow_gust_first of this QueryVmrResultDTO.

        允许来宾先入会。

        :param allow_gust_first: The allow_gust_first of this QueryVmrResultDTO.
        :type allow_gust_first: bool
        """
        self._allow_gust_first = allow_gust_first

    @property
    def gust_first_notice(self):
        """Gets the gust_first_notice of this QueryVmrResultDTO.

        云会议室被使用后是否通知会议室所有者。

        :return: The gust_first_notice of this QueryVmrResultDTO.
        :rtype: bool
        """
        return self._gust_first_notice

    @gust_first_notice.setter
    def gust_first_notice(self, gust_first_notice):
        """Sets the gust_first_notice of this QueryVmrResultDTO.

        云会议室被使用后是否通知会议室所有者。

        :param gust_first_notice: The gust_first_notice of this QueryVmrResultDTO.
        :type gust_first_notice: bool
        """
        self._gust_first_notice = gust_first_notice

    @property
    def vmr_mode(self):
        """Gets the vmr_mode of this QueryVmrResultDTO.

        VMR模式。 * 0: 个人会议ID * 1: 云会议室 * 2: 网络研讨会 

        :return: The vmr_mode of this QueryVmrResultDTO.
        :rtype: int
        """
        return self._vmr_mode

    @vmr_mode.setter
    def vmr_mode(self, vmr_mode):
        """Sets the vmr_mode of this QueryVmrResultDTO.

        VMR模式。 * 0: 个人会议ID * 1: 云会议室 * 2: 网络研讨会 

        :param vmr_mode: The vmr_mode of this QueryVmrResultDTO.
        :type vmr_mode: int
        """
        self._vmr_mode = vmr_mode

    @property
    def vmr_pkg_id(self):
        """Gets the vmr_pkg_id of this QueryVmrResultDTO.

        云会议室套餐包的id，仅云会议室返回。

        :return: The vmr_pkg_id of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._vmr_pkg_id

    @vmr_pkg_id.setter
    def vmr_pkg_id(self, vmr_pkg_id):
        """Sets the vmr_pkg_id of this QueryVmrResultDTO.

        云会议室套餐包的id，仅云会议室返回。

        :param vmr_pkg_id: The vmr_pkg_id of this QueryVmrResultDTO.
        :type vmr_pkg_id: str
        """
        self._vmr_pkg_id = vmr_pkg_id

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this QueryVmrResultDTO.

        云会议室套餐包的名称，仅云会议室返回。

        :return: The vmr_pkg_name of this QueryVmrResultDTO.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this QueryVmrResultDTO.

        云会议室套餐包的名称，仅云会议室返回。

        :param vmr_pkg_name: The vmr_pkg_name of this QueryVmrResultDTO.
        :type vmr_pkg_name: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def vmr_pkg_parties(self):
        """Gets the vmr_pkg_parties of this QueryVmrResultDTO.

        云会议室套餐包的会议并发方数，仅云会议室返回。

        :return: The vmr_pkg_parties of this QueryVmrResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_parties

    @vmr_pkg_parties.setter
    def vmr_pkg_parties(self, vmr_pkg_parties):
        """Sets the vmr_pkg_parties of this QueryVmrResultDTO.

        云会议室套餐包的会议并发方数，仅云会议室返回。

        :param vmr_pkg_parties: The vmr_pkg_parties of this QueryVmrResultDTO.
        :type vmr_pkg_parties: int
        """
        self._vmr_pkg_parties = vmr_pkg_parties

    @property
    def status(self):
        """Gets the status of this QueryVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：停用 * 2：未分配 

        :return: The status of this QueryVmrResultDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：停用 * 2：未分配 

        :param status: The status of this QueryVmrResultDTO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, QueryVmrResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
