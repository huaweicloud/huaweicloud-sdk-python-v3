# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportStatsOpenRequest:

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
        'body': 'ExportVo'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, body=None):
        r"""ExportStatsOpenRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param body: Body of the ExportStatsOpenRequest
        :type body: :class:`huaweicloudsdkcdn.v2.ExportVo`
        """
        
        

        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportStatsOpenRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ExportStatsOpenRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportStatsOpenRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ExportStatsOpenRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this ExportStatsOpenRequest.

        :return: The body of this ExportStatsOpenRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.ExportVo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExportStatsOpenRequest.

        :param body: The body of this ExportStatsOpenRequest.
        :type body: :class:`huaweicloudsdkcdn.v2.ExportVo`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExportStatsOpenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
