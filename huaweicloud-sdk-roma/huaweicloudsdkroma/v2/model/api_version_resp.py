# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiVersionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'version_no': 'str',
        'api_id': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'remark': 'str',
        'publish_time': 'datetime',
        'status': 'int'
    }

    attribute_map = {
        'version_id': 'version_id',
        'version_no': 'version_no',
        'api_id': 'api_id',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'remark': 'remark',
        'publish_time': 'publish_time',
        'status': 'status'
    }

    def __init__(self, version_id=None, version_no=None, api_id=None, env_id=None, env_name=None, remark=None, publish_time=None, status=None):
        """ApiVersionResp

        The model defined in huaweicloud sdk

        :param version_id: API历史版本的ID
        :type version_id: str
        :param version_no: API的版本号
        :type version_no: str
        :param api_id: API编号
        :type api_id: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param env_name: 发布的环境名称
        :type env_name: str
        :param remark: 发布描述
        :type remark: str
        :param publish_time: 发布时间
        :type publish_time: datetime
        :param status: 版本状态 - 1：当前生效中的版本 - 2：未生效的版本
        :type status: int
        """
        
        

        self._version_id = None
        self._version_no = None
        self._api_id = None
        self._env_id = None
        self._env_name = None
        self._remark = None
        self._publish_time = None
        self._status = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if version_no is not None:
            self.version_no = version_no
        if api_id is not None:
            self.api_id = api_id
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if remark is not None:
            self.remark = remark
        if publish_time is not None:
            self.publish_time = publish_time
        if status is not None:
            self.status = status

    @property
    def version_id(self):
        """Gets the version_id of this ApiVersionResp.

        API历史版本的ID

        :return: The version_id of this ApiVersionResp.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ApiVersionResp.

        API历史版本的ID

        :param version_id: The version_id of this ApiVersionResp.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_no(self):
        """Gets the version_no of this ApiVersionResp.

        API的版本号

        :return: The version_no of this ApiVersionResp.
        :rtype: str
        """
        return self._version_no

    @version_no.setter
    def version_no(self, version_no):
        """Sets the version_no of this ApiVersionResp.

        API的版本号

        :param version_no: The version_no of this ApiVersionResp.
        :type version_no: str
        """
        self._version_no = version_no

    @property
    def api_id(self):
        """Gets the api_id of this ApiVersionResp.

        API编号

        :return: The api_id of this ApiVersionResp.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ApiVersionResp.

        API编号

        :param api_id: The api_id of this ApiVersionResp.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def env_id(self):
        """Gets the env_id of this ApiVersionResp.

        发布的环境编号

        :return: The env_id of this ApiVersionResp.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ApiVersionResp.

        发布的环境编号

        :param env_id: The env_id of this ApiVersionResp.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this ApiVersionResp.

        发布的环境名称

        :return: The env_name of this ApiVersionResp.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this ApiVersionResp.

        发布的环境名称

        :param env_name: The env_name of this ApiVersionResp.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def remark(self):
        """Gets the remark of this ApiVersionResp.

        发布描述

        :return: The remark of this ApiVersionResp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiVersionResp.

        发布描述

        :param remark: The remark of this ApiVersionResp.
        :type remark: str
        """
        self._remark = remark

    @property
    def publish_time(self):
        """Gets the publish_time of this ApiVersionResp.

        发布时间

        :return: The publish_time of this ApiVersionResp.
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this ApiVersionResp.

        发布时间

        :param publish_time: The publish_time of this ApiVersionResp.
        :type publish_time: datetime
        """
        self._publish_time = publish_time

    @property
    def status(self):
        """Gets the status of this ApiVersionResp.

        版本状态 - 1：当前生效中的版本 - 2：未生效的版本

        :return: The status of this ApiVersionResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiVersionResp.

        版本状态 - 1：当前生效中的版本 - 2：未生效的版本

        :param status: The status of this ApiVersionResp.
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
        if not isinstance(other, ApiVersionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
