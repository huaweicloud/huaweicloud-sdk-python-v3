# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOriginHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'enterprise_project_id': 'str',
        'body': 'OriginHostRequest'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, domain_id=None, enterprise_project_id=None, body=None):
        r"""UpdateOriginHostRequest

        The model defined in huaweicloud sdk

        :param domain_id: 加速域名ID。
        :type domain_id: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示修改当前企业项目下加速域名的配置，\&quot;all\&quot;代表所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        :param body: Body of the UpdateOriginHostRequest
        :type body: :class:`huaweicloudsdkcdn.v1.OriginHostRequest`
        """
        
        

        self._domain_id = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateOriginHostRequest.

        加速域名ID。

        :return: The domain_id of this UpdateOriginHostRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateOriginHostRequest.

        加速域名ID。

        :param domain_id: The domain_id of this UpdateOriginHostRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateOriginHostRequest.

        当用户开启企业项目功能时，该参数生效，表示修改当前企业项目下加速域名的配置，\"all\"代表所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this UpdateOriginHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateOriginHostRequest.

        当用户开启企业项目功能时，该参数生效，表示修改当前企业项目下加速域名的配置，\"all\"代表所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this UpdateOriginHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this UpdateOriginHostRequest.

        :return: The body of this UpdateOriginHostRequest.
        :rtype: :class:`huaweicloudsdkcdn.v1.OriginHostRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateOriginHostRequest.

        :param body: The body of this UpdateOriginHostRequest.
        :type body: :class:`huaweicloudsdkcdn.v1.OriginHostRequest`
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
        if not isinstance(other, UpdateOriginHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
