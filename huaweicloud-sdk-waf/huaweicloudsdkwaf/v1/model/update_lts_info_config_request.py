# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLtsInfoConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'ltsconfig_id': 'str',
        'body': 'UpdateLtsInfoConfigRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'ltsconfig_id': 'ltsconfig_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, ltsconfig_id=None, body=None):
        """UpdateLtsInfoConfigRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param ltsconfig_id: lts配置信息id，通过ShowLtsInfoConfig获取
        :type ltsconfig_id: str
        :param body: Body of the UpdateLtsInfoConfigRequest
        :type body: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._ltsconfig_id = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.ltsconfig_id = ltsconfig_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateLtsInfoConfigRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this UpdateLtsInfoConfigRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateLtsInfoConfigRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this UpdateLtsInfoConfigRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ltsconfig_id(self):
        """Gets the ltsconfig_id of this UpdateLtsInfoConfigRequest.

        lts配置信息id，通过ShowLtsInfoConfig获取

        :return: The ltsconfig_id of this UpdateLtsInfoConfigRequest.
        :rtype: str
        """
        return self._ltsconfig_id

    @ltsconfig_id.setter
    def ltsconfig_id(self, ltsconfig_id):
        """Sets the ltsconfig_id of this UpdateLtsInfoConfigRequest.

        lts配置信息id，通过ShowLtsInfoConfig获取

        :param ltsconfig_id: The ltsconfig_id of this UpdateLtsInfoConfigRequest.
        :type ltsconfig_id: str
        """
        self._ltsconfig_id = ltsconfig_id

    @property
    def body(self):
        """Gets the body of this UpdateLtsInfoConfigRequest.

        :return: The body of this UpdateLtsInfoConfigRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateLtsInfoConfigRequest.

        :param body: The body of this UpdateLtsInfoConfigRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigRequestBody`
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
        if not isinstance(other, UpdateLtsInfoConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
