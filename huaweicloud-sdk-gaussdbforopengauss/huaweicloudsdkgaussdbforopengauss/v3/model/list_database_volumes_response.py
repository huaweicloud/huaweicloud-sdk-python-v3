# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseVolumesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_volumes': 'list[DatabaseVolumeResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'database_volumes': 'database_volumes',
        'total_count': 'total_count'
    }

    def __init__(self, database_volumes=None, total_count=None):
        r"""ListDatabaseVolumesResponse

        The model defined in huaweicloud sdk

        :param database_volumes: **参数解释**: 数据库占用空间列表。 
        :type database_volumes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVolumeResult`]
        :param total_count: **参数解释**: 总数。 **取值范围**: 不涉及。 
        :type total_count: int
        """
        
        super().__init__()

        self._database_volumes = None
        self._total_count = None
        self.discriminator = None

        if database_volumes is not None:
            self.database_volumes = database_volumes
        if total_count is not None:
            self.total_count = total_count

    @property
    def database_volumes(self):
        r"""Gets the database_volumes of this ListDatabaseVolumesResponse.

        **参数解释**: 数据库占用空间列表。 

        :return: The database_volumes of this ListDatabaseVolumesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVolumeResult`]
        """
        return self._database_volumes

    @database_volumes.setter
    def database_volumes(self, database_volumes):
        r"""Sets the database_volumes of this ListDatabaseVolumesResponse.

        **参数解释**: 数据库占用空间列表。 

        :param database_volumes: The database_volumes of this ListDatabaseVolumesResponse.
        :type database_volumes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVolumeResult`]
        """
        self._database_volumes = database_volumes

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDatabaseVolumesResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :return: The total_count of this ListDatabaseVolumesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDatabaseVolumesResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :param total_count: The total_count of this ListDatabaseVolumesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListDatabaseVolumesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListDatabaseVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
