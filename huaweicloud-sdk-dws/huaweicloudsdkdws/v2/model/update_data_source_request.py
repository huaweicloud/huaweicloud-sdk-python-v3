# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDataSourceRequest:

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
        'ext_data_source_id': 'str',
        'body': 'ReconfigureExtDataSourceAction'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'ext_data_source_id': 'ext_data_source_id',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, ext_data_source_id=None, body=None):
        """UpdateDataSourceRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param ext_data_source_id: 数据源id
        :type ext_data_source_id: str
        :param body: Body of the UpdateDataSourceRequest
        :type body: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
        """
        
        

        self._cluster_id = None
        self._ext_data_source_id = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.ext_data_source_id = ext_data_source_id
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateDataSourceRequest.

        集群ID

        :return: The cluster_id of this UpdateDataSourceRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateDataSourceRequest.

        集群ID

        :param cluster_id: The cluster_id of this UpdateDataSourceRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def ext_data_source_id(self):
        """Gets the ext_data_source_id of this UpdateDataSourceRequest.

        数据源id

        :return: The ext_data_source_id of this UpdateDataSourceRequest.
        :rtype: str
        """
        return self._ext_data_source_id

    @ext_data_source_id.setter
    def ext_data_source_id(self, ext_data_source_id):
        """Sets the ext_data_source_id of this UpdateDataSourceRequest.

        数据源id

        :param ext_data_source_id: The ext_data_source_id of this UpdateDataSourceRequest.
        :type ext_data_source_id: str
        """
        self._ext_data_source_id = ext_data_source_id

    @property
    def body(self):
        """Gets the body of this UpdateDataSourceRequest.

        :return: The body of this UpdateDataSourceRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDataSourceRequest.

        :param body: The body of this UpdateDataSourceRequest.
        :type body: :class:`huaweicloudsdkdws.v2.ReconfigureExtDataSourceAction`
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
        if not isinstance(other, UpdateDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other