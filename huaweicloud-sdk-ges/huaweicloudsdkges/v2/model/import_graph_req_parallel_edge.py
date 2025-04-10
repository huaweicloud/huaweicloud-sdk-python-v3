# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportGraphReqParallelEdge:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'ignore_label': 'bool',
        'sort_key_column': 'str'
    }

    attribute_map = {
        'action': 'action',
        'ignore_label': 'ignore_label',
        'sort_key_column': 'sort_key_column'
    }

    def __init__(self, action=None, ignore_label=None, sort_key_column=None):
        r"""ImportGraphReqParallelEdge

        The model defined in huaweicloud sdk

        :param action: 处理方式，取值为allow，ignore和override，默认为allow。  - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。 图规格为（一千亿边）的图暂不支持该参数。
        :type action: str
        :param ignore_label: 重复边的定义，是否忽略Label。取值为true或者false，默认取true。  - true 表示重复边定义不包含Label，即用&lt;源点，终点&gt;标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用&lt;源点，终点，Label&gt;标记一条边。 图规格为（一千亿边）的图暂不支持该参数。
        :type ignore_label: bool
        :param sort_key_column: sortKey在边文件中的位置，当前仅支持\&quot;lastColumn\&quot;，边文件中无sortKey时，不传此参数。
        :type sort_key_column: str
        """
        
        

        self._action = None
        self._ignore_label = None
        self._sort_key_column = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if ignore_label is not None:
            self.ignore_label = ignore_label
        if sort_key_column is not None:
            self.sort_key_column = sort_key_column

    @property
    def action(self):
        r"""Gets the action of this ImportGraphReqParallelEdge.

        处理方式，取值为allow，ignore和override，默认为allow。  - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。 图规格为（一千亿边）的图暂不支持该参数。

        :return: The action of this ImportGraphReqParallelEdge.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ImportGraphReqParallelEdge.

        处理方式，取值为allow，ignore和override，默认为allow。  - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。 图规格为（一千亿边）的图暂不支持该参数。

        :param action: The action of this ImportGraphReqParallelEdge.
        :type action: str
        """
        self._action = action

    @property
    def ignore_label(self):
        r"""Gets the ignore_label of this ImportGraphReqParallelEdge.

        重复边的定义，是否忽略Label。取值为true或者false，默认取true。  - true 表示重复边定义不包含Label，即用<源点，终点>标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用<源点，终点，Label>标记一条边。 图规格为（一千亿边）的图暂不支持该参数。

        :return: The ignore_label of this ImportGraphReqParallelEdge.
        :rtype: bool
        """
        return self._ignore_label

    @ignore_label.setter
    def ignore_label(self, ignore_label):
        r"""Sets the ignore_label of this ImportGraphReqParallelEdge.

        重复边的定义，是否忽略Label。取值为true或者false，默认取true。  - true 表示重复边定义不包含Label，即用<源点，终点>标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用<源点，终点，Label>标记一条边。 图规格为（一千亿边）的图暂不支持该参数。

        :param ignore_label: The ignore_label of this ImportGraphReqParallelEdge.
        :type ignore_label: bool
        """
        self._ignore_label = ignore_label

    @property
    def sort_key_column(self):
        r"""Gets the sort_key_column of this ImportGraphReqParallelEdge.

        sortKey在边文件中的位置，当前仅支持\"lastColumn\"，边文件中无sortKey时，不传此参数。

        :return: The sort_key_column of this ImportGraphReqParallelEdge.
        :rtype: str
        """
        return self._sort_key_column

    @sort_key_column.setter
    def sort_key_column(self, sort_key_column):
        r"""Sets the sort_key_column of this ImportGraphReqParallelEdge.

        sortKey在边文件中的位置，当前仅支持\"lastColumn\"，边文件中无sortKey时，不传此参数。

        :param sort_key_column: The sort_key_column of this ImportGraphReqParallelEdge.
        :type sort_key_column: str
        """
        self._sort_key_column = sort_key_column

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
        if not isinstance(other, ImportGraphReqParallelEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
