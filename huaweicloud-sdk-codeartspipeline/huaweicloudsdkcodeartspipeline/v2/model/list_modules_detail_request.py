# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModulesDetailRequest:

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
        'name': 'str',
        'product_line': 'str',
        'tags': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'locations': 'list[str]'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'region_name': 'region_name',
        'name': 'name',
        'product_line': 'productLine',
        'tags': 'tags',
        'offset': 'offset',
        'limit': 'limit',
        'locations': 'locations'
    }

    def __init__(self, project_uuid=None, region_name=None, name=None, product_line=None, tags=None, offset=None, limit=None, locations=None):
        r"""ListModulesDetailRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param region_name: 区域名
        :type region_name: str
        :param name: 名称
        :type name: str
        :param product_line: 产品线
        :type product_line: str
        :param tags: 标签
        :type tags: list[str]
        :param offset: 页码
        :type offset: int
        :param limit: 每页显示数
        :type limit: int
        :param locations: 扩展点
        :type locations: list[str]
        """
        
        

        self._project_uuid = None
        self._region_name = None
        self._name = None
        self._product_line = None
        self._tags = None
        self._offset = None
        self._limit = None
        self._locations = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if region_name is not None:
            self.region_name = region_name
        if name is not None:
            self.name = name
        if product_line is not None:
            self.product_line = product_line
        if tags is not None:
            self.tags = tags
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.locations = locations

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListModulesDetailRequest.

        项目uuid

        :return: The project_uuid of this ListModulesDetailRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListModulesDetailRequest.

        项目uuid

        :param project_uuid: The project_uuid of this ListModulesDetailRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def region_name(self):
        r"""Gets the region_name of this ListModulesDetailRequest.

        区域名

        :return: The region_name of this ListModulesDetailRequest.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ListModulesDetailRequest.

        区域名

        :param region_name: The region_name of this ListModulesDetailRequest.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def name(self):
        r"""Gets the name of this ListModulesDetailRequest.

        名称

        :return: The name of this ListModulesDetailRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListModulesDetailRequest.

        名称

        :param name: The name of this ListModulesDetailRequest.
        :type name: str
        """
        self._name = name

    @property
    def product_line(self):
        r"""Gets the product_line of this ListModulesDetailRequest.

        产品线

        :return: The product_line of this ListModulesDetailRequest.
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        r"""Sets the product_line of this ListModulesDetailRequest.

        产品线

        :param product_line: The product_line of this ListModulesDetailRequest.
        :type product_line: str
        """
        self._product_line = product_line

    @property
    def tags(self):
        r"""Gets the tags of this ListModulesDetailRequest.

        标签

        :return: The tags of this ListModulesDetailRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListModulesDetailRequest.

        标签

        :param tags: The tags of this ListModulesDetailRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def offset(self):
        r"""Gets the offset of this ListModulesDetailRequest.

        页码

        :return: The offset of this ListModulesDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModulesDetailRequest.

        页码

        :param offset: The offset of this ListModulesDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListModulesDetailRequest.

        每页显示数

        :return: The limit of this ListModulesDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModulesDetailRequest.

        每页显示数

        :param limit: The limit of this ListModulesDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def locations(self):
        r"""Gets the locations of this ListModulesDetailRequest.

        扩展点

        :return: The locations of this ListModulesDetailRequest.
        :rtype: list[str]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        r"""Sets the locations of this ListModulesDetailRequest.

        扩展点

        :param locations: The locations of this ListModulesDetailRequest.
        :type locations: list[str]
        """
        self._locations = locations

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
        if not isinstance(other, ListModulesDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
