# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAzByInstanceTypeRequest:

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
        'inst_type': 'str',
        'body': 'UpdateAzByInstanceTypeReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'inst_type': 'inst_type',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, inst_type=None, body=None):
        """UpdateAzByInstanceTypeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 待切换AZ的集群ID。
        :type cluster_id: str
        :param inst_type: 待切换AZ的节点类型。支持: - all：所有节点类型。 - ess： 数据节点。 - ess-cold: 冷数据节点。 - ess-client: Client节点。 - ess-master: Master节点。
        :type inst_type: str
        :param body: Body of the UpdateAzByInstanceTypeRequest
        :type body: :class:`huaweicloudsdkcss.v1.UpdateAzByInstanceTypeReq`
        """
        
        

        self._cluster_id = None
        self._inst_type = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.inst_type = inst_type
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateAzByInstanceTypeRequest.

        待切换AZ的集群ID。

        :return: The cluster_id of this UpdateAzByInstanceTypeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateAzByInstanceTypeRequest.

        待切换AZ的集群ID。

        :param cluster_id: The cluster_id of this UpdateAzByInstanceTypeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def inst_type(self):
        """Gets the inst_type of this UpdateAzByInstanceTypeRequest.

        待切换AZ的节点类型。支持: - all：所有节点类型。 - ess： 数据节点。 - ess-cold: 冷数据节点。 - ess-client: Client节点。 - ess-master: Master节点。

        :return: The inst_type of this UpdateAzByInstanceTypeRequest.
        :rtype: str
        """
        return self._inst_type

    @inst_type.setter
    def inst_type(self, inst_type):
        """Sets the inst_type of this UpdateAzByInstanceTypeRequest.

        待切换AZ的节点类型。支持: - all：所有节点类型。 - ess： 数据节点。 - ess-cold: 冷数据节点。 - ess-client: Client节点。 - ess-master: Master节点。

        :param inst_type: The inst_type of this UpdateAzByInstanceTypeRequest.
        :type inst_type: str
        """
        self._inst_type = inst_type

    @property
    def body(self):
        """Gets the body of this UpdateAzByInstanceTypeRequest.

        :return: The body of this UpdateAzByInstanceTypeRequest.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateAzByInstanceTypeReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAzByInstanceTypeRequest.

        :param body: The body of this UpdateAzByInstanceTypeRequest.
        :type body: :class:`huaweicloudsdkcss.v1.UpdateAzByInstanceTypeReq`
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
        if not isinstance(other, UpdateAzByInstanceTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
