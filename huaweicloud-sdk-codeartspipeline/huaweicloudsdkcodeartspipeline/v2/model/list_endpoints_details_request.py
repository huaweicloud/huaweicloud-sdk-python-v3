# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'region_name': 'str',
        'module_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'region_name': 'region_name',
        'module_id': 'module_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_uuid=None, region_name=None, module_id=None, offset=None, limit=None):
        r"""ListEndpointsDetailsRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param region_name: 区域名
        :type region_name: str
        :param module_id: 模块id
        :type module_id: str
        :param offset: 页码
        :type offset: int
        :param limit: 每页显示数
        :type limit: int
        """
        
        

        self._project_uuid = None
        self._region_name = None
        self._module_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.region_name = region_name
        if module_id is not None:
            self.module_id = module_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListEndpointsDetailsRequest.

        项目uuid

        :return: The project_uuid of this ListEndpointsDetailsRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListEndpointsDetailsRequest.

        项目uuid

        :param project_uuid: The project_uuid of this ListEndpointsDetailsRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def region_name(self):
        r"""Gets the region_name of this ListEndpointsDetailsRequest.

        区域名

        :return: The region_name of this ListEndpointsDetailsRequest.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ListEndpointsDetailsRequest.

        区域名

        :param region_name: The region_name of this ListEndpointsDetailsRequest.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def module_id(self):
        r"""Gets the module_id of this ListEndpointsDetailsRequest.

        模块id

        :return: The module_id of this ListEndpointsDetailsRequest.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this ListEndpointsDetailsRequest.

        模块id

        :param module_id: The module_id of this ListEndpointsDetailsRequest.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def offset(self):
        r"""Gets the offset of this ListEndpointsDetailsRequest.

        页码

        :return: The offset of this ListEndpointsDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEndpointsDetailsRequest.

        页码

        :param offset: The offset of this ListEndpointsDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEndpointsDetailsRequest.

        每页显示数

        :return: The limit of this ListEndpointsDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEndpointsDetailsRequest.

        每页显示数

        :param limit: The limit of this ListEndpointsDetailsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEndpointsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
