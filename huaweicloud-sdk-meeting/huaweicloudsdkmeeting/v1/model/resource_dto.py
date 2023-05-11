# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDTO:

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
        'type': 'str',
        'type_id': 'str',
        'count': 'int',
        'expire_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'type_id': 'typeId',
        'count': 'count',
        'expire_date': 'expireDate'
    }

    def __init__(self, id=None, type=None, type_id=None, count=None, expire_date=None):
        """ResourceDTO

        The model defined in huaweicloud sdk

        :param id: 资源标识，不携带则后台自动生成。
        :type id: str
        :param type: 资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub
        :type type: str
        :param type_id: 类型标识，比如资源类型为vmr，vmr又分为5方，10方等，该参数为vmrPkgId，用来区分子类别，详见如下： - vmr10:ff808081699b56d40169c410d5080179 - vmr50:ff808081699b56cb0169c411a0980152 - vmr100:ff808081699b56cb0169c41167850151 - vmr200:ff808081699b56d40169c410913d0178 - vmr25:ff808081699b56d40169c4111fe5017a - vmr300:ff8080816b9ec3ab016bdff237962e83 - vmr400:ff8080816b9ec475016bdff37efc279f - vmr500:ff8080816b9ec3ab016bdff338542e84
        :type type_id: str
        :param count: 资源数量。
        :type count: int
        :param expire_date: 到期时间,utc时间戳。
        :type expire_date: int
        """
        
        

        self._id = None
        self._type = None
        self._type_id = None
        self._count = None
        self._expire_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        if type_id is not None:
            self.type_id = type_id
        self.count = count
        self.expire_date = expire_date

    @property
    def id(self):
        """Gets the id of this ResourceDTO.

        资源标识，不携带则后台自动生成。

        :return: The id of this ResourceDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceDTO.

        资源标识，不携带则后台自动生成。

        :param id: The id of this ResourceDTO.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ResourceDTO.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :return: The type of this ResourceDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceDTO.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :param type: The type of this ResourceDTO.
        :type type: str
        """
        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this ResourceDTO.

        类型标识，比如资源类型为vmr，vmr又分为5方，10方等，该参数为vmrPkgId，用来区分子类别，详见如下： - vmr10:ff808081699b56d40169c410d5080179 - vmr50:ff808081699b56cb0169c411a0980152 - vmr100:ff808081699b56cb0169c41167850151 - vmr200:ff808081699b56d40169c410913d0178 - vmr25:ff808081699b56d40169c4111fe5017a - vmr300:ff8080816b9ec3ab016bdff237962e83 - vmr400:ff8080816b9ec475016bdff37efc279f - vmr500:ff8080816b9ec3ab016bdff338542e84

        :return: The type_id of this ResourceDTO.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ResourceDTO.

        类型标识，比如资源类型为vmr，vmr又分为5方，10方等，该参数为vmrPkgId，用来区分子类别，详见如下： - vmr10:ff808081699b56d40169c410d5080179 - vmr50:ff808081699b56cb0169c411a0980152 - vmr100:ff808081699b56cb0169c41167850151 - vmr200:ff808081699b56d40169c410913d0178 - vmr25:ff808081699b56d40169c4111fe5017a - vmr300:ff8080816b9ec3ab016bdff237962e83 - vmr400:ff8080816b9ec475016bdff37efc279f - vmr500:ff8080816b9ec3ab016bdff338542e84

        :param type_id: The type_id of this ResourceDTO.
        :type type_id: str
        """
        self._type_id = type_id

    @property
    def count(self):
        """Gets the count of this ResourceDTO.

        资源数量。

        :return: The count of this ResourceDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ResourceDTO.

        资源数量。

        :param count: The count of this ResourceDTO.
        :type count: int
        """
        self._count = count

    @property
    def expire_date(self):
        """Gets the expire_date of this ResourceDTO.

        到期时间,utc时间戳。

        :return: The expire_date of this ResourceDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this ResourceDTO.

        到期时间,utc时间戳。

        :param expire_date: The expire_date of this ResourceDTO.
        :type expire_date: int
        """
        self._expire_date = expire_date

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
        if not isinstance(other, ResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
