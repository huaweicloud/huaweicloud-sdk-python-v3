# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableMetaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_metas': 'list[TableMeta]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'table_metas': 'table_metas',
        'page_info': 'page_info'
    }

    def __init__(self, table_metas=None, page_info=None):
        """ListTableMetaResponse

        The model defined in huaweicloud sdk

        :param table_metas: 
        :type table_metas: list[:class:`huaweicloudsdklakeformation.v1.TableMeta`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(ListTableMetaResponse, self).__init__()

        self._table_metas = None
        self._page_info = None
        self.discriminator = None

        if table_metas is not None:
            self.table_metas = table_metas
        if page_info is not None:
            self.page_info = page_info

    @property
    def table_metas(self):
        """Gets the table_metas of this ListTableMetaResponse.

        :return: The table_metas of this ListTableMetaResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.TableMeta`]
        """
        return self._table_metas

    @table_metas.setter
    def table_metas(self, table_metas):
        """Sets the table_metas of this ListTableMetaResponse.

        :param table_metas: The table_metas of this ListTableMetaResponse.
        :type table_metas: list[:class:`huaweicloudsdklakeformation.v1.TableMeta`]
        """
        self._table_metas = table_metas

    @property
    def page_info(self):
        """Gets the page_info of this ListTableMetaResponse.

        :return: The page_info of this ListTableMetaResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListTableMetaResponse.

        :param page_info: The page_info of this ListTableMetaResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListTableMetaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
