# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpdLabelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'label_type': 'str',
        'title': 'str',
        'category_types': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'label_type': 'label_type',
        'title': 'title',
        'category_types': 'category_types'
    }

    def __init__(self, project_id=None, label_type=None, title=None, category_types=None):
        r"""ListIpdLabelsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param label_type: 标签归属的工作项分类，不传该参数时默认查询所有类型下的标签。不推荐使用此参数，建议使用category_types参数。
        :type label_type: str
        :param title: 标签名称
        :type title: str
        :param category_types: 工作项类型编码。
        :type category_types: str
        """
        
        

        self._project_id = None
        self._label_type = None
        self._title = None
        self._category_types = None
        self.discriminator = None

        self.project_id = project_id
        if label_type is not None:
            self.label_type = label_type
        if title is not None:
            self.title = title
        if category_types is not None:
            self.category_types = category_types

    @property
    def project_id(self):
        r"""Gets the project_id of this ListIpdLabelsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ListIpdLabelsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListIpdLabelsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ListIpdLabelsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def label_type(self):
        r"""Gets the label_type of this ListIpdLabelsRequest.

        标签归属的工作项分类，不传该参数时默认查询所有类型下的标签。不推荐使用此参数，建议使用category_types参数。

        :return: The label_type of this ListIpdLabelsRequest.
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        r"""Sets the label_type of this ListIpdLabelsRequest.

        标签归属的工作项分类，不传该参数时默认查询所有类型下的标签。不推荐使用此参数，建议使用category_types参数。

        :param label_type: The label_type of this ListIpdLabelsRequest.
        :type label_type: str
        """
        self._label_type = label_type

    @property
    def title(self):
        r"""Gets the title of this ListIpdLabelsRequest.

        标签名称

        :return: The title of this ListIpdLabelsRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListIpdLabelsRequest.

        标签名称

        :param title: The title of this ListIpdLabelsRequest.
        :type title: str
        """
        self._title = title

    @property
    def category_types(self):
        r"""Gets the category_types of this ListIpdLabelsRequest.

        工作项类型编码。

        :return: The category_types of this ListIpdLabelsRequest.
        :rtype: str
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        r"""Sets the category_types of this ListIpdLabelsRequest.

        工作项类型编码。

        :param category_types: The category_types of this ListIpdLabelsRequest.
        :type category_types: str
        """
        self._category_types = category_types

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
        if not isinstance(other, ListIpdLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
