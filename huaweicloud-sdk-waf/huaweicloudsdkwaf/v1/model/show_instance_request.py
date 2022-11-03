# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceRequest:

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
        'instance_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'instance_id': 'instance_id'
    }

    def __init__(self, enterprise_project_id=None, instance_id=None):
        """ShowInstanceRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询企业项目ID
        :type enterprise_project_id: str
        :param instance_id: 独享引擎ID（通过调用WAF的ListInstance接口获取所有独享引擎信息查询独享引擎ID）
        :type instance_id: str
        """
        
        

        self._enterprise_project_id = None
        self._instance_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.instance_id = instance_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowInstanceRequest.

        通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询企业项目ID

        :return: The enterprise_project_id of this ShowInstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowInstanceRequest.

        通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询通过企业项目管理服务的查询企业项目列表接口ListEnterpriseProject查询企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceRequest.

        独享引擎ID（通过调用WAF的ListInstance接口获取所有独享引擎信息查询独享引擎ID）

        :return: The instance_id of this ShowInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceRequest.

        独享引擎ID（通过调用WAF的ListInstance接口获取所有独享引擎信息查询独享引擎ID）

        :param instance_id: The instance_id of this ShowInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
