# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowValueListRequest:

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
        'valuelistid': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'valuelistid': 'valuelistid'
    }

    def __init__(self, enterprise_project_id=None, valuelistid=None):
        r"""ShowValueListRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param valuelistid: 引用表id，通过查询引用表列表（ListValueList）接口获取
        :type valuelistid: str
        """
        
        

        self._enterprise_project_id = None
        self._valuelistid = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.valuelistid = valuelistid

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowValueListRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ShowValueListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowValueListRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ShowValueListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def valuelistid(self):
        r"""Gets the valuelistid of this ShowValueListRequest.

        引用表id，通过查询引用表列表（ListValueList）接口获取

        :return: The valuelistid of this ShowValueListRequest.
        :rtype: str
        """
        return self._valuelistid

    @valuelistid.setter
    def valuelistid(self, valuelistid):
        r"""Sets the valuelistid of this ShowValueListRequest.

        引用表id，通过查询引用表列表（ListValueList）接口获取

        :param valuelistid: The valuelistid of this ShowValueListRequest.
        :type valuelistid: str
        """
        self._valuelistid = valuelistid

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
        if not isinstance(other, ShowValueListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
