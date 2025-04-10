# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafAttackEventlist:

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
        'domain': 'str',
        'time': 'int',
        'sip': 'str',
        'action': 'str',
        'url': 'str',
        'type': 'str',
        'backend': 'Backend'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'time': 'time',
        'sip': 'sip',
        'action': 'action',
        'url': 'url',
        'type': 'type',
        'backend': 'backend'
    }

    def __init__(self, id=None, domain=None, time=None, sip=None, action=None, url=None, type=None, backend=None):
        r"""ListWafAttackEventlist

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param domain: 攻击目标域名
        :type domain: str
        :param time: 攻击时间
        :type time: int
        :param sip: 攻击源IP
        :type sip: str
        :param action: 防御动作
        :type action: str
        :param url: 攻击url
        :type url: str
        :param type: 攻击类型
        :type type: str
        :param backend: 
        :type backend: :class:`huaweicloudsdkaad.v2.Backend`
        """
        
        

        self._id = None
        self._domain = None
        self._time = None
        self._sip = None
        self._action = None
        self._url = None
        self._type = None
        self._backend = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if time is not None:
            self.time = time
        if sip is not None:
            self.sip = sip
        if action is not None:
            self.action = action
        if url is not None:
            self.url = url
        if type is not None:
            self.type = type
        if backend is not None:
            self.backend = backend

    @property
    def id(self):
        r"""Gets the id of this ListWafAttackEventlist.

        id

        :return: The id of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListWafAttackEventlist.

        id

        :param id: The id of this ListWafAttackEventlist.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        r"""Gets the domain of this ListWafAttackEventlist.

        攻击目标域名

        :return: The domain of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListWafAttackEventlist.

        攻击目标域名

        :param domain: The domain of this ListWafAttackEventlist.
        :type domain: str
        """
        self._domain = domain

    @property
    def time(self):
        r"""Gets the time of this ListWafAttackEventlist.

        攻击时间

        :return: The time of this ListWafAttackEventlist.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListWafAttackEventlist.

        攻击时间

        :param time: The time of this ListWafAttackEventlist.
        :type time: int
        """
        self._time = time

    @property
    def sip(self):
        r"""Gets the sip of this ListWafAttackEventlist.

        攻击源IP

        :return: The sip of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        r"""Sets the sip of this ListWafAttackEventlist.

        攻击源IP

        :param sip: The sip of this ListWafAttackEventlist.
        :type sip: str
        """
        self._sip = sip

    @property
    def action(self):
        r"""Gets the action of this ListWafAttackEventlist.

        防御动作

        :return: The action of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListWafAttackEventlist.

        防御动作

        :param action: The action of this ListWafAttackEventlist.
        :type action: str
        """
        self._action = action

    @property
    def url(self):
        r"""Gets the url of this ListWafAttackEventlist.

        攻击url

        :return: The url of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ListWafAttackEventlist.

        攻击url

        :param url: The url of this ListWafAttackEventlist.
        :type url: str
        """
        self._url = url

    @property
    def type(self):
        r"""Gets the type of this ListWafAttackEventlist.

        攻击类型

        :return: The type of this ListWafAttackEventlist.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListWafAttackEventlist.

        攻击类型

        :param type: The type of this ListWafAttackEventlist.
        :type type: str
        """
        self._type = type

    @property
    def backend(self):
        r"""Gets the backend of this ListWafAttackEventlist.

        :return: The backend of this ListWafAttackEventlist.
        :rtype: :class:`huaweicloudsdkaad.v2.Backend`
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        r"""Sets the backend of this ListWafAttackEventlist.

        :param backend: The backend of this ListWafAttackEventlist.
        :type backend: :class:`huaweicloudsdkaad.v2.Backend`
        """
        self._backend = backend

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
        if not isinstance(other, ListWafAttackEventlist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
