# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtcUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app': 'str',
        'room_id': 'str',
        'uid': 'str',
        'session': 'str',
        'state': 'str',
        'nick_name': 'str',
        'ip': 'str',
        'region': 'str',
        'isp': 'str',
        'device_model': 'str',
        'platform': 'str',
        'sdk': 'str',
        'join_time': 'str',
        'leave_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'room_id': 'room_id',
        'uid': 'uid',
        'session': 'session',
        'state': 'state',
        'nick_name': 'nick_name',
        'ip': 'ip',
        'region': 'region',
        'isp': 'isp',
        'device_model': 'device_model',
        'platform': 'platform',
        'sdk': 'sdk',
        'join_time': 'join_time',
        'leave_time': 'leave_time'
    }

    def __init__(self, domain=None, app=None, room_id=None, uid=None, session=None, state=None, nick_name=None, ip=None, region=None, isp=None, device_model=None, platform=None, sdk=None, join_time=None, leave_time=None):
        """RtcUser

        The model defined in huaweicloud sdk

        :param domain: 域名
        :type domain: str
        :param app: 应用标识
        :type app: str
        :param room_id: 房间ID
        :type room_id: str
        :param uid: 用户id
        :type uid: str
        :param session: 会话id
        :type session: str
        :param state: 用户状态   - FAIL： 加入失败   - ONLINE：在线   - OFFLINE：离开 
        :type state: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param ip: 用户接入IP
        :type ip: str
        :param region: 用户接入IP所在省份
        :type region: str
        :param isp: 用户接入IP所在运营商
        :type isp: str
        :param device_model: 用户设备型号
        :type device_model: str
        :param platform: 用户设备平台
        :type platform: str
        :param sdk: 用户sdk版本
        :type sdk: str
        :param join_time: 用户加入房间时间。格式为：YYYY-MM-DDThh:mm:ssZ 
        :type join_time: str
        :param leave_time: 用户离开房间时间。格式为：YYYY-MM-DDThh:mm:ssZ，若用户未离开，则返回 “-” 
        :type leave_time: str
        """
        
        

        self._domain = None
        self._app = None
        self._room_id = None
        self._uid = None
        self._session = None
        self._state = None
        self._nick_name = None
        self._ip = None
        self._region = None
        self._isp = None
        self._device_model = None
        self._platform = None
        self._sdk = None
        self._join_time = None
        self._leave_time = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if app is not None:
            self.app = app
        if room_id is not None:
            self.room_id = room_id
        if uid is not None:
            self.uid = uid
        if session is not None:
            self.session = session
        if state is not None:
            self.state = state
        if nick_name is not None:
            self.nick_name = nick_name
        if ip is not None:
            self.ip = ip
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if device_model is not None:
            self.device_model = device_model
        if platform is not None:
            self.platform = platform
        if sdk is not None:
            self.sdk = sdk
        if join_time is not None:
            self.join_time = join_time
        if leave_time is not None:
            self.leave_time = leave_time

    @property
    def domain(self):
        """Gets the domain of this RtcUser.

        域名

        :return: The domain of this RtcUser.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RtcUser.

        域名

        :param domain: The domain of this RtcUser.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        """Gets the app of this RtcUser.

        应用标识

        :return: The app of this RtcUser.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RtcUser.

        应用标识

        :param app: The app of this RtcUser.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this RtcUser.

        房间ID

        :return: The room_id of this RtcUser.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this RtcUser.

        房间ID

        :param room_id: The room_id of this RtcUser.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def uid(self):
        """Gets the uid of this RtcUser.

        用户id

        :return: The uid of this RtcUser.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this RtcUser.

        用户id

        :param uid: The uid of this RtcUser.
        :type uid: str
        """
        self._uid = uid

    @property
    def session(self):
        """Gets the session of this RtcUser.

        会话id

        :return: The session of this RtcUser.
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this RtcUser.

        会话id

        :param session: The session of this RtcUser.
        :type session: str
        """
        self._session = session

    @property
    def state(self):
        """Gets the state of this RtcUser.

        用户状态   - FAIL： 加入失败   - ONLINE：在线   - OFFLINE：离开 

        :return: The state of this RtcUser.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RtcUser.

        用户状态   - FAIL： 加入失败   - ONLINE：在线   - OFFLINE：离开 

        :param state: The state of this RtcUser.
        :type state: str
        """
        self._state = state

    @property
    def nick_name(self):
        """Gets the nick_name of this RtcUser.

        用户昵称

        :return: The nick_name of this RtcUser.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this RtcUser.

        用户昵称

        :param nick_name: The nick_name of this RtcUser.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def ip(self):
        """Gets the ip of this RtcUser.

        用户接入IP

        :return: The ip of this RtcUser.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this RtcUser.

        用户接入IP

        :param ip: The ip of this RtcUser.
        :type ip: str
        """
        self._ip = ip

    @property
    def region(self):
        """Gets the region of this RtcUser.

        用户接入IP所在省份

        :return: The region of this RtcUser.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RtcUser.

        用户接入IP所在省份

        :param region: The region of this RtcUser.
        :type region: str
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this RtcUser.

        用户接入IP所在运营商

        :return: The isp of this RtcUser.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this RtcUser.

        用户接入IP所在运营商

        :param isp: The isp of this RtcUser.
        :type isp: str
        """
        self._isp = isp

    @property
    def device_model(self):
        """Gets the device_model of this RtcUser.

        用户设备型号

        :return: The device_model of this RtcUser.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this RtcUser.

        用户设备型号

        :param device_model: The device_model of this RtcUser.
        :type device_model: str
        """
        self._device_model = device_model

    @property
    def platform(self):
        """Gets the platform of this RtcUser.

        用户设备平台

        :return: The platform of this RtcUser.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this RtcUser.

        用户设备平台

        :param platform: The platform of this RtcUser.
        :type platform: str
        """
        self._platform = platform

    @property
    def sdk(self):
        """Gets the sdk of this RtcUser.

        用户sdk版本

        :return: The sdk of this RtcUser.
        :rtype: str
        """
        return self._sdk

    @sdk.setter
    def sdk(self, sdk):
        """Sets the sdk of this RtcUser.

        用户sdk版本

        :param sdk: The sdk of this RtcUser.
        :type sdk: str
        """
        self._sdk = sdk

    @property
    def join_time(self):
        """Gets the join_time of this RtcUser.

        用户加入房间时间。格式为：YYYY-MM-DDThh:mm:ssZ 

        :return: The join_time of this RtcUser.
        :rtype: str
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this RtcUser.

        用户加入房间时间。格式为：YYYY-MM-DDThh:mm:ssZ 

        :param join_time: The join_time of this RtcUser.
        :type join_time: str
        """
        self._join_time = join_time

    @property
    def leave_time(self):
        """Gets the leave_time of this RtcUser.

        用户离开房间时间。格式为：YYYY-MM-DDThh:mm:ssZ，若用户未离开，则返回 “-” 

        :return: The leave_time of this RtcUser.
        :rtype: str
        """
        return self._leave_time

    @leave_time.setter
    def leave_time(self, leave_time):
        """Sets the leave_time of this RtcUser.

        用户离开房间时间。格式为：YYYY-MM-DDThh:mm:ssZ，若用户未离开，则返回 “-” 

        :param leave_time: The leave_time of this RtcUser.
        :type leave_time: str
        """
        self._leave_time = leave_time

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
        if not isinstance(other, RtcUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
