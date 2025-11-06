# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTenantRepositoryBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_ids': 'list[int]'
    }

    attribute_map = {
        'repository_ids': 'repository_ids'
    }

    def __init__(self, repository_ids=None):
        r"""ExportTenantRepositoryBody

        The model defined in huaweicloud sdk

        :param repository_ids: 
        :type repository_ids: list[int]
        """
        
        

        self._repository_ids = None
        self.discriminator = None

        if repository_ids is not None:
            self.repository_ids = repository_ids

    @property
    def repository_ids(self):
        r"""Gets the repository_ids of this ExportTenantRepositoryBody.

        :return: The repository_ids of this ExportTenantRepositoryBody.
        :rtype: list[int]
        """
        return self._repository_ids

    @repository_ids.setter
    def repository_ids(self, repository_ids):
        r"""Sets the repository_ids of this ExportTenantRepositoryBody.

        :param repository_ids: The repository_ids of this ExportTenantRepositoryBody.
        :type repository_ids: list[int]
        """
        self._repository_ids = repository_ids

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
        if not isinstance(other, ExportTenantRepositoryBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
