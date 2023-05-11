# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'name': 'str',
        'status': 'int',
        'app_key': 'str',
        'creator': 'str',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'app_key': 'app_key',
        'creator': 'creator',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, name=None, status=None, app_key=None, creator=None, precise_search=None):
        """ListAppsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param id: APP编号
        :type id: str
        :param name: APP名称
        :type name: str
        :param status: APP状态
        :type status: int
        :param app_key: APP的KEY
        :type app_key: str
        :param creator: APP的创建者。 - USER：用户自行创建 - MARKET：[云商店分配](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)
        :type creator: str
        :param precise_search: 指定需要精确匹配查找的参数名称，目前仅支持name
        :type precise_search: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._status = None
        self._app_key = None
        self._creator = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if app_key is not None:
            self.app_key = app_key
        if creator is not None:
            self.creator = creator
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAppsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListAppsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAppsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListAppsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListAppsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListAppsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListAppsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAppsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListAppsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListAppsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this ListAppsV2Request.

        APP编号

        :return: The id of this ListAppsV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAppsV2Request.

        APP编号

        :param id: The id of this ListAppsV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAppsV2Request.

        APP名称

        :return: The name of this ListAppsV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAppsV2Request.

        APP名称

        :param name: The name of this ListAppsV2Request.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListAppsV2Request.

        APP状态

        :return: The status of this ListAppsV2Request.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAppsV2Request.

        APP状态

        :param status: The status of this ListAppsV2Request.
        :type status: int
        """
        self._status = status

    @property
    def app_key(self):
        """Gets the app_key of this ListAppsV2Request.

        APP的KEY

        :return: The app_key of this ListAppsV2Request.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ListAppsV2Request.

        APP的KEY

        :param app_key: The app_key of this ListAppsV2Request.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def creator(self):
        """Gets the creator of this ListAppsV2Request.

        APP的创建者。 - USER：用户自行创建 - MARKET：[云商店分配](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :return: The creator of this ListAppsV2Request.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListAppsV2Request.

        APP的创建者。 - USER：用户自行创建 - MARKET：[云商店分配](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :param creator: The creator of this ListAppsV2Request.
        :type creator: str
        """
        self._creator = creator

    @property
    def precise_search(self):
        """Gets the precise_search of this ListAppsV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :return: The precise_search of this ListAppsV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListAppsV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :param precise_search: The precise_search of this ListAppsV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListAppsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
