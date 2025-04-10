# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'asset_id': 'str',
        'parent_id': 'str',
        'body': 'CommRequestAssetTree'
    }

    attribute_map = {
        'project_id': 'project_id',
        'asset_id': 'asset_id',
        'parent_id': 'parent_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, asset_id=None, parent_id=None, body=None):
        r"""CreateAssetTreeRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param asset_id: 资产ID
        :type asset_id: str
        :param parent_id: 父目录ID
        :type parent_id: str
        :param body: Body of the CreateAssetTreeRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.CommRequestAssetTree`
        """
        
        

        self._project_id = None
        self._asset_id = None
        self._parent_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.asset_id = asset_id
        self.parent_id = parent_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateAssetTreeRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this CreateAssetTreeRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateAssetTreeRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this CreateAssetTreeRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this CreateAssetTreeRequest.

        资产ID

        :return: The asset_id of this CreateAssetTreeRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this CreateAssetTreeRequest.

        资产ID

        :param asset_id: The asset_id of this CreateAssetTreeRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CreateAssetTreeRequest.

        父目录ID

        :return: The parent_id of this CreateAssetTreeRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CreateAssetTreeRequest.

        父目录ID

        :param parent_id: The parent_id of this CreateAssetTreeRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def body(self):
        r"""Gets the body of this CreateAssetTreeRequest.

        :return: The body of this CreateAssetTreeRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommRequestAssetTree`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAssetTreeRequest.

        :param body: The body of this CreateAssetTreeRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.CommRequestAssetTree`
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
        if not isinstance(other, CreateAssetTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
