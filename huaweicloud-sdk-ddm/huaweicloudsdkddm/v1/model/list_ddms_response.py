# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_num': 'int',
        'instances': 'list[CustomerInstanceVO]',
        'page_size': 'int',
        'total': 'int',
        'total_page': 'int',
        'page_no': 'int'
    }

    attribute_map = {
        'instance_num': 'instance_num',
        'instances': 'instances',
        'page_size': 'page_size',
        'total': 'total',
        'total_page': 'total_page',
        'page_no': 'page_no'
    }

    def __init__(self, instance_num=None, instances=None, page_size=None, total=None, total_page=None, page_no=None):
        r"""ListDdmsResponse

        The model defined in huaweicloud sdk

        :param instance_num: **参数解释**：  实例数量。  **参数范围**：  不涉及。
        :type instance_num: int
        :param instances: **参数解释**：  实例列表的集合。  **参数范围**：  不涉及。
        :type instances: list[:class:`huaweicloudsdkddm.v1.CustomerInstanceVO`]
        :param page_size: **参数解释**：  分页大小。  **参数范围**：  不涉及。
        :type page_size: int
        :param total: **参数解释**：  实例总量。  **参数范围**：  不涉及。
        :type total: int
        :param total_page: **参数解释**：  总分页数。  **参数范围**：  不涉及。
        :type total_page: int
        :param page_no: **参数解释**：  分页序号。  **参数范围**：  不涉及。
        :type page_no: int
        """
        
        super().__init__()

        self._instance_num = None
        self._instances = None
        self._page_size = None
        self._total = None
        self._total_page = None
        self._page_no = None
        self.discriminator = None

        if instance_num is not None:
            self.instance_num = instance_num
        if instances is not None:
            self.instances = instances
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total
        if total_page is not None:
            self.total_page = total_page
        if page_no is not None:
            self.page_no = page_no

    @property
    def instance_num(self):
        r"""Gets the instance_num of this ListDdmsResponse.

        **参数解释**：  实例数量。  **参数范围**：  不涉及。

        :return: The instance_num of this ListDdmsResponse.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this ListDdmsResponse.

        **参数解释**：  实例数量。  **参数范围**：  不涉及。

        :param instance_num: The instance_num of this ListDdmsResponse.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def instances(self):
        r"""Gets the instances of this ListDdmsResponse.

        **参数解释**：  实例列表的集合。  **参数范围**：  不涉及。

        :return: The instances of this ListDdmsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.CustomerInstanceVO`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListDdmsResponse.

        **参数解释**：  实例列表的集合。  **参数范围**：  不涉及。

        :param instances: The instances of this ListDdmsResponse.
        :type instances: list[:class:`huaweicloudsdkddm.v1.CustomerInstanceVO`]
        """
        self._instances = instances

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDdmsResponse.

        **参数解释**：  分页大小。  **参数范围**：  不涉及。

        :return: The page_size of this ListDdmsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDdmsResponse.

        **参数解释**：  分页大小。  **参数范围**：  不涉及。

        :param page_size: The page_size of this ListDdmsResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total(self):
        r"""Gets the total of this ListDdmsResponse.

        **参数解释**：  实例总量。  **参数范围**：  不涉及。

        :return: The total of this ListDdmsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDdmsResponse.

        **参数解释**：  实例总量。  **参数范围**：  不涉及。

        :param total: The total of this ListDdmsResponse.
        :type total: int
        """
        self._total = total

    @property
    def total_page(self):
        r"""Gets the total_page of this ListDdmsResponse.

        **参数解释**：  总分页数。  **参数范围**：  不涉及。

        :return: The total_page of this ListDdmsResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        r"""Sets the total_page of this ListDdmsResponse.

        **参数解释**：  总分页数。  **参数范围**：  不涉及。

        :param total_page: The total_page of this ListDdmsResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def page_no(self):
        r"""Gets the page_no of this ListDdmsResponse.

        **参数解释**：  分页序号。  **参数范围**：  不涉及。

        :return: The page_no of this ListDdmsResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListDdmsResponse.

        **参数解释**：  分页序号。  **参数范围**：  不涉及。

        :param page_no: The page_no of this ListDdmsResponse.
        :type page_no: int
        """
        self._page_no = page_no

    def to_dict(self):
        import warnings
        warnings.warn("ListDdmsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDdmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
