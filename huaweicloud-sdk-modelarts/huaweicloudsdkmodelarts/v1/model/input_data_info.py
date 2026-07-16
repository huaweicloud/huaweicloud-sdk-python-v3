# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset': 'InputDataInfoDataset',
        'obs': 'InputDataInfoObs'
    }

    attribute_map = {
        'dataset': 'dataset',
        'obs': 'obs'
    }

    def __init__(self, dataset=None, obs=None):
        r"""InputDataInfo

        The model defined in huaweicloud sdk

        :param dataset: 
        :type dataset: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoDataset`
        :param obs: 
        :type obs: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoObs`
        """
        
        

        self._dataset = None
        self._obs = None
        self.discriminator = None

        if dataset is not None:
            self.dataset = dataset
        if obs is not None:
            self.obs = obs

    @property
    def dataset(self):
        r"""Gets the dataset of this InputDataInfo.

        :return: The dataset of this InputDataInfo.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoDataset`
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        r"""Sets the dataset of this InputDataInfo.

        :param dataset: The dataset of this InputDataInfo.
        :type dataset: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoDataset`
        """
        self._dataset = dataset

    @property
    def obs(self):
        r"""Gets the obs of this InputDataInfo.

        :return: The obs of this InputDataInfo.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this InputDataInfo.

        :param obs: The obs of this InputDataInfo.
        :type obs: :class:`huaweicloudsdkmodelarts.v1.InputDataInfoObs`
        """
        self._obs = obs

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
        if not isinstance(other, InputDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
