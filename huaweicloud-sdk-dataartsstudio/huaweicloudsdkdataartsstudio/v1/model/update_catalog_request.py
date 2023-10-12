# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCatalogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'catalog_id': 'str',
        'body': 'ApiCatalogUpdateParaDTO'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'catalog_id': 'catalog_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, dlm_type=None, catalog_id=None, body=None):
        """UpdateCatalogRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param catalog_id: 目录编号
        :type catalog_id: str
        :param body: Body of the UpdateCatalogRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApiCatalogUpdateParaDTO`
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._catalog_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        self.catalog_id = catalog_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this UpdateCatalogRequest.

        工作空间id

        :return: The workspace of this UpdateCatalogRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this UpdateCatalogRequest.

        工作空间id

        :param workspace: The workspace of this UpdateCatalogRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this UpdateCatalogRequest.

        dlm版本类型

        :return: The dlm_type of this UpdateCatalogRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this UpdateCatalogRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this UpdateCatalogRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def catalog_id(self):
        """Gets the catalog_id of this UpdateCatalogRequest.

        目录编号

        :return: The catalog_id of this UpdateCatalogRequest.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this UpdateCatalogRequest.

        目录编号

        :param catalog_id: The catalog_id of this UpdateCatalogRequest.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def body(self):
        """Gets the body of this UpdateCatalogRequest.

        :return: The body of this UpdateCatalogRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApiCatalogUpdateParaDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateCatalogRequest.

        :param body: The body of this UpdateCatalogRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApiCatalogUpdateParaDTO`
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
        if not isinstance(other, UpdateCatalogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
