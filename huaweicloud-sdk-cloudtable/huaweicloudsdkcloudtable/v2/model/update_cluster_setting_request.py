# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'x_language': 'str',
        'body': 'HbaseModifySettingV2Req'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, x_language=None, body=None):
        r"""UpdateClusterSettingRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param x_language: 语言类型
        :type x_language: str
        :param body: Body of the UpdateClusterSettingRequest
        :type body: :class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2Req`
        """
        
        

        self._cluster_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateClusterSettingRequest.

        集群ID

        :return: The cluster_id of this UpdateClusterSettingRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateClusterSettingRequest.

        集群ID

        :param cluster_id: The cluster_id of this UpdateClusterSettingRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateClusterSettingRequest.

        语言类型

        :return: The x_language of this UpdateClusterSettingRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateClusterSettingRequest.

        语言类型

        :param x_language: The x_language of this UpdateClusterSettingRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this UpdateClusterSettingRequest.

        :return: The body of this UpdateClusterSettingRequest.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateClusterSettingRequest.

        :param body: The body of this UpdateClusterSettingRequest.
        :type body: :class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2Req`
        """
        self._body = body

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
        if not isinstance(other, UpdateClusterSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
