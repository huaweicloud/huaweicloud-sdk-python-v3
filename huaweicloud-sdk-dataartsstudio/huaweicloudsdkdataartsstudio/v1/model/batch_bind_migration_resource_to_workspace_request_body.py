# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBindMigrationResourceToWorkspaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'banding_resource_list': 'list[MigrationBindResource]'
    }

    attribute_map = {
        'banding_resource_list': 'banding_resource_list'
    }

    def __init__(self, banding_resource_list=None):
        r"""BatchBindMigrationResourceToWorkspaceRequestBody

        The model defined in huaweicloud sdk

        :param banding_resource_list: 待关联或取消关联的资源列表。
        :type banding_resource_list: list[:class:`huaweicloudsdkdataartsstudio.v1.MigrationBindResource`]
        """
        
        

        self._banding_resource_list = None
        self.discriminator = None

        self.banding_resource_list = banding_resource_list

    @property
    def banding_resource_list(self):
        r"""Gets the banding_resource_list of this BatchBindMigrationResourceToWorkspaceRequestBody.

        待关联或取消关联的资源列表。

        :return: The banding_resource_list of this BatchBindMigrationResourceToWorkspaceRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MigrationBindResource`]
        """
        return self._banding_resource_list

    @banding_resource_list.setter
    def banding_resource_list(self, banding_resource_list):
        r"""Sets the banding_resource_list of this BatchBindMigrationResourceToWorkspaceRequestBody.

        待关联或取消关联的资源列表。

        :param banding_resource_list: The banding_resource_list of this BatchBindMigrationResourceToWorkspaceRequestBody.
        :type banding_resource_list: list[:class:`huaweicloudsdkdataartsstudio.v1.MigrationBindResource`]
        """
        self._banding_resource_list = banding_resource_list

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
        if not isinstance(other, BatchBindMigrationResourceToWorkspaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
