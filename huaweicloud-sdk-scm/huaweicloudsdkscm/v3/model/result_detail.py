# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'total_num': 'int',
        'deployed_resources': 'list[DeployedResourceDetail]'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'total_num': 'total_num',
        'deployed_resources': 'deployed_resources'
    }

    def __init__(self, certificate_id=None, total_num=None, deployed_resources=None):
        r"""ResultDetail

        The model defined in huaweicloud sdk

        :param certificate_id: 证书ID。
        :type certificate_id: str
        :param total_num: 当前证书在所查询服务中已部署资源总数。
        :type total_num: int
        :param deployed_resources: 当前证书已部署资源列表，详情请参见DeployedResourceDetail字段数据结构说明。
        :type deployed_resources: list[:class:`huaweicloudsdkscm.v3.DeployedResourceDetail`]
        """
        
        

        self._certificate_id = None
        self._total_num = None
        self._deployed_resources = None
        self.discriminator = None

        self.certificate_id = certificate_id
        self.total_num = total_num
        self.deployed_resources = deployed_resources

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this ResultDetail.

        证书ID。

        :return: The certificate_id of this ResultDetail.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this ResultDetail.

        证书ID。

        :param certificate_id: The certificate_id of this ResultDetail.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def total_num(self):
        r"""Gets the total_num of this ResultDetail.

        当前证书在所查询服务中已部署资源总数。

        :return: The total_num of this ResultDetail.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ResultDetail.

        当前证书在所查询服务中已部署资源总数。

        :param total_num: The total_num of this ResultDetail.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def deployed_resources(self):
        r"""Gets the deployed_resources of this ResultDetail.

        当前证书已部署资源列表，详情请参见DeployedResourceDetail字段数据结构说明。

        :return: The deployed_resources of this ResultDetail.
        :rtype: list[:class:`huaweicloudsdkscm.v3.DeployedResourceDetail`]
        """
        return self._deployed_resources

    @deployed_resources.setter
    def deployed_resources(self, deployed_resources):
        r"""Sets the deployed_resources of this ResultDetail.

        当前证书已部署资源列表，详情请参见DeployedResourceDetail字段数据结构说明。

        :param deployed_resources: The deployed_resources of this ResultDetail.
        :type deployed_resources: list[:class:`huaweicloudsdkscm.v3.DeployedResourceDetail`]
        """
        self._deployed_resources = deployed_resources

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
        if not isinstance(other, ResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
