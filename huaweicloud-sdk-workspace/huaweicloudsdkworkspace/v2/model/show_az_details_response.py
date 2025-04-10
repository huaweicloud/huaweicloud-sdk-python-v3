# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAzDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'region_id': 'str',
        'type': 'str',
        'display_name': 'str',
        'status': 'str',
        'sold_out': 'SoldOutInfo',
        'product_ids': 'list[str]',
        'mode': 'str',
        'alias': 'str',
        'public_border_group': 'str',
        'category': 'int'
    }

    attribute_map = {
        'id': 'id',
        'region_id': 'region_id',
        'type': 'type',
        'display_name': 'display_name',
        'status': 'status',
        'sold_out': 'sold_out',
        'product_ids': 'product_ids',
        'mode': 'mode',
        'alias': 'alias',
        'public_border_group': 'public_border_group',
        'category': 'category'
    }

    def __init__(self, id=None, region_id=None, type=None, display_name=None, status=None, sold_out=None, product_ids=None, mode=None, alias=None, public_border_group=None, category=None):
        r"""ShowAzDetailsResponse

        The model defined in huaweicloud sdk

        :param id: 对应CMDB的region数据中的&#39;zoneCode&#39;字段。
        :type id: str
        :param region_id: 对应CMDB的region数据中的&#39;regionCode&#39;字段。
        :type region_id: str
        :param type: 当前AZ的类型: - Edge: 边缘云 - Workspace：华为云
        :type type: str
        :param display_name: 英文名。
        :type display_name: str
        :param status: 状态。
        :type status: str
        :param sold_out: 
        :type sold_out: :class:`huaweicloudsdkworkspace.v2.SoldOutInfo`
        :param product_ids: 参品Id集。
        :type product_ids: list[str]
        :param mode: 计费模式，专属 / 共享。
        :type mode: str
        :param alias: az的别名(中文、数字、字母、下划线、中划线，最大128字节)。
        :type alias: str
        :param public_border_group: EIP所属的group。
        :type public_border_group: str
        :param category: 分类的Id:  - 0: default - 21: HomeZone - 41: IES
        :type category: int
        """
        
        super(ShowAzDetailsResponse, self).__init__()

        self._id = None
        self._region_id = None
        self._type = None
        self._display_name = None
        self._status = None
        self._sold_out = None
        self._product_ids = None
        self._mode = None
        self._alias = None
        self._public_border_group = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if region_id is not None:
            self.region_id = region_id
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if status is not None:
            self.status = status
        if sold_out is not None:
            self.sold_out = sold_out
        if product_ids is not None:
            self.product_ids = product_ids
        if mode is not None:
            self.mode = mode
        if alias is not None:
            self.alias = alias
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this ShowAzDetailsResponse.

        对应CMDB的region数据中的'zoneCode'字段。

        :return: The id of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAzDetailsResponse.

        对应CMDB的region数据中的'zoneCode'字段。

        :param id: The id of this ShowAzDetailsResponse.
        :type id: str
        """
        self._id = id

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAzDetailsResponse.

        对应CMDB的region数据中的'regionCode'字段。

        :return: The region_id of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAzDetailsResponse.

        对应CMDB的region数据中的'regionCode'字段。

        :param region_id: The region_id of this ShowAzDetailsResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def type(self):
        r"""Gets the type of this ShowAzDetailsResponse.

        当前AZ的类型: - Edge: 边缘云 - Workspace：华为云

        :return: The type of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAzDetailsResponse.

        当前AZ的类型: - Edge: 边缘云 - Workspace：华为云

        :param type: The type of this ShowAzDetailsResponse.
        :type type: str
        """
        self._type = type

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowAzDetailsResponse.

        英文名。

        :return: The display_name of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowAzDetailsResponse.

        英文名。

        :param display_name: The display_name of this ShowAzDetailsResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def status(self):
        r"""Gets the status of this ShowAzDetailsResponse.

        状态。

        :return: The status of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAzDetailsResponse.

        状态。

        :param status: The status of this ShowAzDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def sold_out(self):
        r"""Gets the sold_out of this ShowAzDetailsResponse.

        :return: The sold_out of this ShowAzDetailsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SoldOutInfo`
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        r"""Sets the sold_out of this ShowAzDetailsResponse.

        :param sold_out: The sold_out of this ShowAzDetailsResponse.
        :type sold_out: :class:`huaweicloudsdkworkspace.v2.SoldOutInfo`
        """
        self._sold_out = sold_out

    @property
    def product_ids(self):
        r"""Gets the product_ids of this ShowAzDetailsResponse.

        参品Id集。

        :return: The product_ids of this ShowAzDetailsResponse.
        :rtype: list[str]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        r"""Sets the product_ids of this ShowAzDetailsResponse.

        参品Id集。

        :param product_ids: The product_ids of this ShowAzDetailsResponse.
        :type product_ids: list[str]
        """
        self._product_ids = product_ids

    @property
    def mode(self):
        r"""Gets the mode of this ShowAzDetailsResponse.

        计费模式，专属 / 共享。

        :return: The mode of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShowAzDetailsResponse.

        计费模式，专属 / 共享。

        :param mode: The mode of this ShowAzDetailsResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def alias(self):
        r"""Gets the alias of this ShowAzDetailsResponse.

        az的别名(中文、数字、字母、下划线、中划线，最大128字节)。

        :return: The alias of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ShowAzDetailsResponse.

        az的别名(中文、数字、字母、下划线、中划线，最大128字节)。

        :param alias: The alias of this ShowAzDetailsResponse.
        :type alias: str
        """
        self._alias = alias

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ShowAzDetailsResponse.

        EIP所属的group。

        :return: The public_border_group of this ShowAzDetailsResponse.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ShowAzDetailsResponse.

        EIP所属的group。

        :param public_border_group: The public_border_group of this ShowAzDetailsResponse.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def category(self):
        r"""Gets the category of this ShowAzDetailsResponse.

        分类的Id:  - 0: default - 21: HomeZone - 41: IES

        :return: The category of this ShowAzDetailsResponse.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowAzDetailsResponse.

        分类的Id:  - 0: default - 21: HomeZone - 41: IES

        :param category: The category of this ShowAzDetailsResponse.
        :type category: int
        """
        self._category = category

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
        if not isinstance(other, ShowAzDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
