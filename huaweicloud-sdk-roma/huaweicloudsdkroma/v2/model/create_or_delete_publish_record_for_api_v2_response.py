# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrDeletePublishRecordForApiV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_id': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'env_id': 'str',
        'remark': 'str',
        'publish_time': 'datetime',
        'version_id': 'str'
    }

    attribute_map = {
        'publish_id': 'publish_id',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'env_id': 'env_id',
        'remark': 'remark',
        'publish_time': 'publish_time',
        'version_id': 'version_id'
    }

    def __init__(self, publish_id=None, api_id=None, api_name=None, env_id=None, remark=None, publish_time=None, version_id=None):
        r"""CreateOrDeletePublishRecordForApiV2Response

        The model defined in huaweicloud sdk

        :param publish_id: 发布记录的ID
        :type publish_id: str
        :param api_id: API编号
        :type api_id: str
        :param api_name: API名称
        :type api_name: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param remark: 发布描述
        :type remark: str
        :param publish_time: 发布时间
        :type publish_time: datetime
        :param version_id: 在线的版本号
        :type version_id: str
        """
        
        super(CreateOrDeletePublishRecordForApiV2Response, self).__init__()

        self._publish_id = None
        self._api_id = None
        self._api_name = None
        self._env_id = None
        self._remark = None
        self._publish_time = None
        self._version_id = None
        self.discriminator = None

        if publish_id is not None:
            self.publish_id = publish_id
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if env_id is not None:
            self.env_id = env_id
        if remark is not None:
            self.remark = remark
        if publish_time is not None:
            self.publish_time = publish_time
        if version_id is not None:
            self.version_id = version_id

    @property
    def publish_id(self):
        r"""Gets the publish_id of this CreateOrDeletePublishRecordForApiV2Response.

        发布记录的ID

        :return: The publish_id of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        r"""Sets the publish_id of this CreateOrDeletePublishRecordForApiV2Response.

        发布记录的ID

        :param publish_id: The publish_id of this CreateOrDeletePublishRecordForApiV2Response.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def api_id(self):
        r"""Gets the api_id of this CreateOrDeletePublishRecordForApiV2Response.

        API编号

        :return: The api_id of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this CreateOrDeletePublishRecordForApiV2Response.

        API编号

        :param api_id: The api_id of this CreateOrDeletePublishRecordForApiV2Response.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        r"""Gets the api_name of this CreateOrDeletePublishRecordForApiV2Response.

        API名称

        :return: The api_name of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this CreateOrDeletePublishRecordForApiV2Response.

        API名称

        :param api_name: The api_name of this CreateOrDeletePublishRecordForApiV2Response.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def env_id(self):
        r"""Gets the env_id of this CreateOrDeletePublishRecordForApiV2Response.

        发布的环境编号

        :return: The env_id of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this CreateOrDeletePublishRecordForApiV2Response.

        发布的环境编号

        :param env_id: The env_id of this CreateOrDeletePublishRecordForApiV2Response.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def remark(self):
        r"""Gets the remark of this CreateOrDeletePublishRecordForApiV2Response.

        发布描述

        :return: The remark of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this CreateOrDeletePublishRecordForApiV2Response.

        发布描述

        :param remark: The remark of this CreateOrDeletePublishRecordForApiV2Response.
        :type remark: str
        """
        self._remark = remark

    @property
    def publish_time(self):
        r"""Gets the publish_time of this CreateOrDeletePublishRecordForApiV2Response.

        发布时间

        :return: The publish_time of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this CreateOrDeletePublishRecordForApiV2Response.

        发布时间

        :param publish_time: The publish_time of this CreateOrDeletePublishRecordForApiV2Response.
        :type publish_time: datetime
        """
        self._publish_time = publish_time

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateOrDeletePublishRecordForApiV2Response.

        在线的版本号

        :return: The version_id of this CreateOrDeletePublishRecordForApiV2Response.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateOrDeletePublishRecordForApiV2Response.

        在线的版本号

        :param version_id: The version_id of this CreateOrDeletePublishRecordForApiV2Response.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, CreateOrDeletePublishRecordForApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
