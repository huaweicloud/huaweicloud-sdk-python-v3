# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table': 'MetricTableItem',
        'metadata': 'ResourceMetricsMetadata'
    }

    attribute_map = {
        'table': 'table',
        'metadata': 'metadata'
    }

    def __init__(self, table=None, metadata=None):
        r"""MetricsItem

        The model defined in huaweicloud sdk

        :param table: 
        :type table: :class:`huaweicloudsdkmodelarts.v1.MetricTableItem`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.ResourceMetricsMetadata`
        """
        
        

        self._table = None
        self._metadata = None
        self.discriminator = None

        if table is not None:
            self.table = table
        if metadata is not None:
            self.metadata = metadata

    @property
    def table(self):
        r"""Gets the table of this MetricsItem.

        :return: The table of this MetricsItem.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MetricTableItem`
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this MetricsItem.

        :param table: The table of this MetricsItem.
        :type table: :class:`huaweicloudsdkmodelarts.v1.MetricTableItem`
        """
        self._table = table

    @property
    def metadata(self):
        r"""Gets the metadata of this MetricsItem.

        :return: The metadata of this MetricsItem.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceMetricsMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this MetricsItem.

        :param metadata: The metadata of this MetricsItem.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.ResourceMetricsMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, MetricsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
