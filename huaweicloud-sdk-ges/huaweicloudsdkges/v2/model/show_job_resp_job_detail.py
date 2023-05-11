# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobRespJobDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_path': 'list[ShowJobRespJobDetailSchemaPath]',
        'edgeset_path': 'list[ShowJobRespJobDetailSchemaPath]',
        'vertexset_path': 'list[ShowJobRespJobDetailSchemaPath]'
    }

    attribute_map = {
        'schema_path': 'schema_path',
        'edgeset_path': 'edgeset_path',
        'vertexset_path': 'vertexset_path'
    }

    def __init__(self, schema_path=None, edgeset_path=None, vertexset_path=None):
        """ShowJobRespJobDetail

        The model defined in huaweicloud sdk

        :param schema_path: 元数据路径。
        :type schema_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        :param edgeset_path: 边数据集路径。
        :type edgeset_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        :param vertexset_path: 点数据集路径。
        :type vertexset_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        
        

        self._schema_path = None
        self._edgeset_path = None
        self._vertexset_path = None
        self.discriminator = None

        if schema_path is not None:
            self.schema_path = schema_path
        if edgeset_path is not None:
            self.edgeset_path = edgeset_path
        if vertexset_path is not None:
            self.vertexset_path = vertexset_path

    @property
    def schema_path(self):
        """Gets the schema_path of this ShowJobRespJobDetail.

        元数据路径。

        :return: The schema_path of this ShowJobRespJobDetail.
        :rtype: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        """Sets the schema_path of this ShowJobRespJobDetail.

        元数据路径。

        :param schema_path: The schema_path of this ShowJobRespJobDetail.
        :type schema_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        self._schema_path = schema_path

    @property
    def edgeset_path(self):
        """Gets the edgeset_path of this ShowJobRespJobDetail.

        边数据集路径。

        :return: The edgeset_path of this ShowJobRespJobDetail.
        :rtype: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        """Sets the edgeset_path of this ShowJobRespJobDetail.

        边数据集路径。

        :param edgeset_path: The edgeset_path of this ShowJobRespJobDetail.
        :type edgeset_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        self._edgeset_path = edgeset_path

    @property
    def vertexset_path(self):
        """Gets the vertexset_path of this ShowJobRespJobDetail.

        点数据集路径。

        :return: The vertexset_path of this ShowJobRespJobDetail.
        :rtype: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        """Sets the vertexset_path of this ShowJobRespJobDetail.

        点数据集路径。

        :param vertexset_path: The vertexset_path of this ShowJobRespJobDetail.
        :type vertexset_path: list[:class:`huaweicloudsdkges.v2.ShowJobRespJobDetailSchemaPath`]
        """
        self._vertexset_path = vertexset_path

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
        if not isinstance(other, ShowJobRespJobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
