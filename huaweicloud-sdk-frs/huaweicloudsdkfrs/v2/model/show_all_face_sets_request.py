# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllFaceSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'Enterprise-Project-Id'
    }

    def __init__(self, enterprise_project_id=None):
        """ShowAllFaceSetsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region&#x3D;cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 &gt; 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。
        :type enterprise_project_id: str
        """
        
        

        self._enterprise_project_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowAllFaceSetsRequest.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。

        :return: The enterprise_project_id of this ShowAllFaceSetsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowAllFaceSetsRequest.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。

        :param enterprise_project_id: The enterprise_project_id of this ShowAllFaceSetsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowAllFaceSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
