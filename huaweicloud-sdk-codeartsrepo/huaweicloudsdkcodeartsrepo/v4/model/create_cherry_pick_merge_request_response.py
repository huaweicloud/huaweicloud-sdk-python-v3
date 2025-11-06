# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCherryPickMergeRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'title': 'str',
        'cherry_pick_branch_name': 'str'
    }

    attribute_map = {
        'state': 'state',
        'title': 'title',
        'cherry_pick_branch_name': 'cherry_pick_branch_name'
    }

    def __init__(self, state=None, title=None, cherry_pick_branch_name=None):
        r"""CreateCherryPickMergeRequestResponse

        The model defined in huaweicloud sdk

        :param state: CherryPick结果
        :type state: str
        :param title: CherryPick标题
        :type title: str
        :param cherry_pick_branch_name: CherryPick临时分支名名称
        :type cherry_pick_branch_name: str
        """
        
        super().__init__()

        self._state = None
        self._title = None
        self._cherry_pick_branch_name = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if cherry_pick_branch_name is not None:
            self.cherry_pick_branch_name = cherry_pick_branch_name

    @property
    def state(self):
        r"""Gets the state of this CreateCherryPickMergeRequestResponse.

        CherryPick结果

        :return: The state of this CreateCherryPickMergeRequestResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateCherryPickMergeRequestResponse.

        CherryPick结果

        :param state: The state of this CreateCherryPickMergeRequestResponse.
        :type state: str
        """
        self._state = state

    @property
    def title(self):
        r"""Gets the title of this CreateCherryPickMergeRequestResponse.

        CherryPick标题

        :return: The title of this CreateCherryPickMergeRequestResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateCherryPickMergeRequestResponse.

        CherryPick标题

        :param title: The title of this CreateCherryPickMergeRequestResponse.
        :type title: str
        """
        self._title = title

    @property
    def cherry_pick_branch_name(self):
        r"""Gets the cherry_pick_branch_name of this CreateCherryPickMergeRequestResponse.

        CherryPick临时分支名名称

        :return: The cherry_pick_branch_name of this CreateCherryPickMergeRequestResponse.
        :rtype: str
        """
        return self._cherry_pick_branch_name

    @cherry_pick_branch_name.setter
    def cherry_pick_branch_name(self, cherry_pick_branch_name):
        r"""Sets the cherry_pick_branch_name of this CreateCherryPickMergeRequestResponse.

        CherryPick临时分支名名称

        :param cherry_pick_branch_name: The cherry_pick_branch_name of this CreateCherryPickMergeRequestResponse.
        :type cherry_pick_branch_name: str
        """
        self._cherry_pick_branch_name = cherry_pick_branch_name

    def to_dict(self):
        import warnings
        warnings.warn("CreateCherryPickMergeRequestResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateCherryPickMergeRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
