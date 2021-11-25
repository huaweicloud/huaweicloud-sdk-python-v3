# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApiGroupV2Response(SdkResponse):


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
        'name': 'str',
        'status': 'int',
        'sl_domain': 'str',
        'register_time': 'datetime',
        'update_time': 'datetime',
        'on_sell_status': 'int',
        'url_domains': 'list[UrlDomain]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'sl_domain': 'sl_domain',
        'register_time': 'register_time',
        'update_time': 'update_time',
        'on_sell_status': 'on_sell_status',
        'url_domains': 'url_domains'
    }

    def __init__(self, id=None, name=None, status=None, sl_domain=None, register_time=None, update_time=None, on_sell_status=None, url_domains=None):
        """CreateApiGroupV2Response - a model defined in huaweicloud sdk"""
        
        super(CreateApiGroupV2Response, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._sl_domain = None
        self._register_time = None
        self._update_time = None
        self._on_sell_status = None
        self._url_domains = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.sl_domain = sl_domain
        self.register_time = register_time
        self.update_time = update_time
        self.on_sell_status = on_sell_status
        if url_domains is not None:
            self.url_domains = url_domains

    @property
    def id(self):
        """Gets the id of this CreateApiGroupV2Response.

        编号

        :return: The id of this CreateApiGroupV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateApiGroupV2Response.

        编号

        :param id: The id of this CreateApiGroupV2Response.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateApiGroupV2Response.

        API分组名称

        :return: The name of this CreateApiGroupV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateApiGroupV2Response.

        API分组名称

        :param name: The name of this CreateApiGroupV2Response.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateApiGroupV2Response.

        状态   - 1： 有效

        :return: The status of this CreateApiGroupV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateApiGroupV2Response.

        状态   - 1： 有效

        :param status: The status of this CreateApiGroupV2Response.
        :type: int
        """
        self._status = status

    @property
    def sl_domain(self):
        """Gets the sl_domain of this CreateApiGroupV2Response.

        系统默认分配的子域名

        :return: The sl_domain of this CreateApiGroupV2Response.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        """Sets the sl_domain of this CreateApiGroupV2Response.

        系统默认分配的子域名

        :param sl_domain: The sl_domain of this CreateApiGroupV2Response.
        :type: str
        """
        self._sl_domain = sl_domain

    @property
    def register_time(self):
        """Gets the register_time of this CreateApiGroupV2Response.

        创建时间

        :return: The register_time of this CreateApiGroupV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this CreateApiGroupV2Response.

        创建时间

        :param register_time: The register_time of this CreateApiGroupV2Response.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateApiGroupV2Response.

        最近修改时间

        :return: The update_time of this CreateApiGroupV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateApiGroupV2Response.

        最近修改时间

        :param update_time: The update_time of this CreateApiGroupV2Response.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def on_sell_status(self):
        """Gets the on_sell_status of this CreateApiGroupV2Response.

        是否已上架云市场： - 1：已上架 - 2：未上架 - 3：审核中  ROMAConnect暂未对接云市场，此字段默认返回2

        :return: The on_sell_status of this CreateApiGroupV2Response.
        :rtype: int
        """
        return self._on_sell_status

    @on_sell_status.setter
    def on_sell_status(self, on_sell_status):
        """Sets the on_sell_status of this CreateApiGroupV2Response.

        是否已上架云市场： - 1：已上架 - 2：未上架 - 3：审核中  ROMAConnect暂未对接云市场，此字段默认返回2

        :param on_sell_status: The on_sell_status of this CreateApiGroupV2Response.
        :type: int
        """
        self._on_sell_status = on_sell_status

    @property
    def url_domains(self):
        """Gets the url_domains of this CreateApiGroupV2Response.

        分组上绑定的独立域名列表

        :return: The url_domains of this CreateApiGroupV2Response.
        :rtype: list[UrlDomain]
        """
        return self._url_domains

    @url_domains.setter
    def url_domains(self, url_domains):
        """Sets the url_domains of this CreateApiGroupV2Response.

        分组上绑定的独立域名列表

        :param url_domains: The url_domains of this CreateApiGroupV2Response.
        :type: list[UrlDomain]
        """
        self._url_domains = url_domains

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
        if not isinstance(other, CreateApiGroupV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
