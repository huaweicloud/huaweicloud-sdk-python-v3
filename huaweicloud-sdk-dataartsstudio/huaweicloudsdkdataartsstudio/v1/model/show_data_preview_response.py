# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataPreviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rows': 'list[list[object]]',
        'schema': 'list[object]'
    }

    attribute_map = {
        'rows': 'rows',
        'schema': 'schema'
    }

    def __init__(self, rows=None, schema=None):
        r"""ShowDataPreviewResponse

        The model defined in huaweicloud sdk

        :param rows: 表中数据信息列表
        :type rows: list[list[object]]
        :param schema: 字段信息列表
        :type schema: list[object]
        """
        
        super(ShowDataPreviewResponse, self).__init__()

        self._rows = None
        self._schema = None
        self.discriminator = None

        if rows is not None:
            self.rows = rows
        if schema is not None:
            self.schema = schema

    @property
    def rows(self):
        r"""Gets the rows of this ShowDataPreviewResponse.

        表中数据信息列表

        :return: The rows of this ShowDataPreviewResponse.
        :rtype: list[list[object]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this ShowDataPreviewResponse.

        表中数据信息列表

        :param rows: The rows of this ShowDataPreviewResponse.
        :type rows: list[list[object]]
        """
        self._rows = rows

    @property
    def schema(self):
        r"""Gets the schema of this ShowDataPreviewResponse.

        字段信息列表

        :return: The schema of this ShowDataPreviewResponse.
        :rtype: list[object]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowDataPreviewResponse.

        字段信息列表

        :param schema: The schema of this ShowDataPreviewResponse.
        :type schema: list[object]
        """
        self._schema = schema

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
        if not isinstance(other, ShowDataPreviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
