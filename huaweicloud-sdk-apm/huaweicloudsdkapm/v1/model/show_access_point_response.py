# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessPointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'gmt_create': 'str',
        'gmt_modify': 'str',
        'region': 'str',
        'access_point': 'str',
        'token': 'str',
        'hidden_token': 'str',
        'sw_business_id': 'int',
        'agent_download_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'region': 'region',
        'access_point': 'accessPoint',
        'token': 'token',
        'hidden_token': 'hidden_token',
        'sw_business_id': 'sw_business_id',
        'agent_download_url': 'agent_download_url'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, region=None, access_point=None, token=None, hidden_token=None, sw_business_id=None, agent_download_url=None):
        """ShowAccessPointResponse

        The model defined in huaweicloud sdk

        :param id: 
        :type id: int
        :param gmt_create: 创建时间
        :type gmt_create: str
        :param gmt_modify: 修改时间
        :type gmt_modify: str
        :param region: 当前局点
        :type region: str
        :param access_point: 接入点地址
        :type access_point: str
        :param token: token
        :type token: str
        :param hidden_token: token隐藏字符
        :type hidden_token: str
        :param sw_business_id: 应用ID
        :type sw_business_id: int
        :param agent_download_url: agent下载地址
        :type agent_download_url: str
        """
        
        super(ShowAccessPointResponse, self).__init__()

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._region = None
        self._access_point = None
        self._token = None
        self._hidden_token = None
        self._sw_business_id = None
        self._agent_download_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if region is not None:
            self.region = region
        if access_point is not None:
            self.access_point = access_point
        if token is not None:
            self.token = token
        if hidden_token is not None:
            self.hidden_token = hidden_token
        if sw_business_id is not None:
            self.sw_business_id = sw_business_id
        if agent_download_url is not None:
            self.agent_download_url = agent_download_url

    @property
    def id(self):
        """Gets the id of this ShowAccessPointResponse.

        :return: The id of this ShowAccessPointResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAccessPointResponse.

        :param id: The id of this ShowAccessPointResponse.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this ShowAccessPointResponse.

        创建时间

        :return: The gmt_create of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this ShowAccessPointResponse.

        创建时间

        :param gmt_create: The gmt_create of this ShowAccessPointResponse.
        :type gmt_create: str
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this ShowAccessPointResponse.

        修改时间

        :return: The gmt_modify of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this ShowAccessPointResponse.

        修改时间

        :param gmt_modify: The gmt_modify of this ShowAccessPointResponse.
        :type gmt_modify: str
        """
        self._gmt_modify = gmt_modify

    @property
    def region(self):
        """Gets the region of this ShowAccessPointResponse.

        当前局点

        :return: The region of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowAccessPointResponse.

        当前局点

        :param region: The region of this ShowAccessPointResponse.
        :type region: str
        """
        self._region = region

    @property
    def access_point(self):
        """Gets the access_point of this ShowAccessPointResponse.

        接入点地址

        :return: The access_point of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this ShowAccessPointResponse.

        接入点地址

        :param access_point: The access_point of this ShowAccessPointResponse.
        :type access_point: str
        """
        self._access_point = access_point

    @property
    def token(self):
        """Gets the token of this ShowAccessPointResponse.

        token

        :return: The token of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ShowAccessPointResponse.

        token

        :param token: The token of this ShowAccessPointResponse.
        :type token: str
        """
        self._token = token

    @property
    def hidden_token(self):
        """Gets the hidden_token of this ShowAccessPointResponse.

        token隐藏字符

        :return: The hidden_token of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._hidden_token

    @hidden_token.setter
    def hidden_token(self, hidden_token):
        """Sets the hidden_token of this ShowAccessPointResponse.

        token隐藏字符

        :param hidden_token: The hidden_token of this ShowAccessPointResponse.
        :type hidden_token: str
        """
        self._hidden_token = hidden_token

    @property
    def sw_business_id(self):
        """Gets the sw_business_id of this ShowAccessPointResponse.

        应用ID

        :return: The sw_business_id of this ShowAccessPointResponse.
        :rtype: int
        """
        return self._sw_business_id

    @sw_business_id.setter
    def sw_business_id(self, sw_business_id):
        """Sets the sw_business_id of this ShowAccessPointResponse.

        应用ID

        :param sw_business_id: The sw_business_id of this ShowAccessPointResponse.
        :type sw_business_id: int
        """
        self._sw_business_id = sw_business_id

    @property
    def agent_download_url(self):
        """Gets the agent_download_url of this ShowAccessPointResponse.

        agent下载地址

        :return: The agent_download_url of this ShowAccessPointResponse.
        :rtype: str
        """
        return self._agent_download_url

    @agent_download_url.setter
    def agent_download_url(self, agent_download_url):
        """Sets the agent_download_url of this ShowAccessPointResponse.

        agent下载地址

        :param agent_download_url: The agent_download_url of this ShowAccessPointResponse.
        :type agent_download_url: str
        """
        self._agent_download_url = agent_download_url

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
        if not isinstance(other, ShowAccessPointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
